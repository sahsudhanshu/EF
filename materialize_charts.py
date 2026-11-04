import os, shutil, sys, runpy
# Windows workspace disallows hard links; publish the validated bytes by copying.
os.link=lambda source,destination: shutil.copyfile(source,destination)
script=r'C:\Users\Sudhanshu\.codex\plugins\cache\openai-primary-runtime\presentations\26.1030.10813\skills\presentations\container_tools\materialize_literal_chart_workbooks.py'
sys.path.insert(0,os.path.dirname(script))
sys.argv=[script,os.path.abspath('slide_build_v4/candidate.pptx'),os.path.abspath('slide_build_v4/portable.pptx'),'--workspace',os.getcwd(),'--receipt',os.path.abspath('slide_build_v4/chart_receipt.json')]
runpy.run_path(script,run_name='__main__')
