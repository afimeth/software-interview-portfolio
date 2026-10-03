"""Run trusted, repository-owned synthetic patches. This is NOT a sandbox."""
import difflib, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def evaluate():
    source=(ROOT/'logic.py').read_text()
    cases=[
        ('correct', source, 'PASS', 'Equivalent formatting refactor; domain and HTTP contract retained.'),
        ('blank_validation_removed', source.replace('not title.strip()', 'False'), 'FAIL', 'Empty titles admitted.'),
        ('wrong_completion', source.replace("task['done'] = True", "task['done'] = False"), 'FAIL', 'Completion acknowledges without changing state.'),
        ('wrong_id', source.replace('len(tasks) + 1', 'len(tasks)'), 'FAIL', 'First ID violates contract and roundtrip.'),
        ('missing_spec', None, 'ABSTAIN', 'Requested priority sorting has no specified order or tie-breaker.'),
    ]
    records=[]
    for name, candidate, expected, diagnosis in cases:
        if candidate is None:
            records.append({'case':name,'expected':expected,'decision':'ABSTAIN','score':None,'reason':diagnosis,'evidence':None});continue
        if name=='correct': candidate=candidate.replace("return title.strip()", "return title.strip()  # preserve contract")
        diff=''.join(difflib.unified_diff(source.splitlines(True),candidate.splitlines(True),fromfile='before/logic.py',tofile='after/logic.py'))
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)
            for filename in ['logic.py','server.py','index.html']: shutil.copy(ROOT/filename,target/filename)
            shutil.copytree(ROOT/'tests',target/'tests',ignore=shutil.ignore_patterns('__pycache__'))
            (target/'logic.py').write_text(candidate,encoding='utf-8')
            result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=target,capture_output=True,text=True,timeout=20)
            output=result.stdout+result.stderr
        decision='PASS' if result.returncode==0 else 'FAIL'
        records.append({'case':name,'expected':expected,'decision':decision,'score':100 if decision=='PASS' else 0,'reason':diagnosis,'patch':diff,'patch_sha256':hashlib.sha256(diff.encode()).hexdigest(),'evidence':{'exit_code':result.returncode,'output':output}})
    return {'schema':'patch-eval/v1','rubric':{'functional_contract':'12 domain/HTTP checks, required gate','scope':'only logic.py; fixed owned fixture','uncertainty':'missing specification => ABSTAIN, never counted as PASS'},'cases':records,'matched_expected':all(r['decision']==r['expected'] for r in records),'limitations':['Synthetic mutations, no live model scoring','No arbitrary patch execution or security sandbox','No semantic judge or model comparison','Static HTML contract check; no browser execution in this fixture','Score is a binary contract gate, not engineering quality ranking']}

if __name__=='__main__':
    receipt=evaluate();print(json.dumps(receipt,indent=2));sys.exit(0 if receipt['matched_expected'] else 1)
