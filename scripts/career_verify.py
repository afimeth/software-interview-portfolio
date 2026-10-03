import hashlib,json,os,re,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'evaluator'))
from evaluate import evaluate

def main():
    suite=unittest.defaultTestLoader.discover(str(ROOT/'evaluator/tests'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    evaluation=evaluate()
    ledger=json.loads((ROOT/'career/CLAIM_REGISTRY.json').read_text())
    for claim in ledger['claims']:
        assert claim['status'] in ['IMPLEMENTED','MEASURED','DESIGNED','RESEARCHED']
        assert re.fullmatch('[0-9a-f]{40}',claim['commit'])
        assert claim['safe_cv_wording'] and claim['avoid'] and claim['recall_prompt'] and claim['evidence']
        assert all(ref.startswith('https://github.com/afimeth/') for ref in claim['evidence'])
    for file in ['PORTFOLIO_INDEX.md','career/CV_A.md','career/CV_B.md','career/CV_C.md','career/APPLICATION_PACKS.md','career/site-cards.json']:
        assert (ROOT/file).is_file(), file
    sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    receipt={'schema':'career-evidence/v1','commit_sha':sha,'tracked_worktree_dirty':bool(subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT,text=True).strip()),'ci_run_url':f"https://github.com/{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ.get('GITHUB_RUN_ID')}" if os.environ.get('GITHUB_RUN_ID') else None,'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'evaluation':evaluation,'claim_count':len(ledger['claims']),'unsupported_claims':['Employment history or years','Production scale','Independent audit','Live provider evaluation','Mainnet ownership','Browser E2E for task fixture']}
    (ROOT/'career-receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    assert result.wasSuccessful() and evaluation['matched_expected']
    print(f'PASS: {result.testsRun} tests; 5 patch/spec cases; {len(ledger["claims"])} claim mappings')
if __name__=='__main__': main()
