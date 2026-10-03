import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1];d=json.loads((p/'PORTFOLIO_RECEIPT.json').read_text())
repos={r['name']:r for r in d['repositories']}
assert len(repos)==8 and len(d['targets'])==6
for r in repos.values():
 assert not r['is_private'] and re.fullmatch('[0-9a-f]{40}',r['head_sha'])
 assert r['ci']['headSha']==r['head_sha'] and r['ci']['conclusion']=='success'
 assert len(r['jobs'])==4 and all(j['conclusion']=='success' for j in r['jobs'])
assert len(d['ci_receipts'])==20
for r in d['ci_receipts']:assert r['passed'] and not r['dirty'] and r['sha']==repos[r['repo']]['head_sha']
for t in d['targets']:
 assert t['safe_cv_claim'] and t['remaining_gap'] and t['estimated_interview_readiness']
 for scenario in t['scenarios']:
  assert scenario['evidence']
  for e in scenario['evidence']:assert e['commit_sha']==repos[e['repo']]['head_sha'] and e['ci_status']=='success'
assert d['lab_ci_jobs_passed']==sum(len(r['jobs']) for r in repos.values())==32
assert all((p/n).is_file() for n in ['README.md','PORTFOLIO_COVERAGE.md','APPLICATION_READY.md'])
print('PASS: 8 exact lab heads, 32 successful CI jobs, 20 matching receipts, 6 role-family mappings')
