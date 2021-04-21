find -name ScenarioBase* -delete
find -name ScenarioRunBase* -delete
find -name *AllOf* -delete
find -name *Details* -delete
find -name UserDetails* -delete
find -name ScenarioRunContainers* -delete
git add .
git commit -am "Doc for inherited domain class + ScenarioRunContainers=>ScenarioRunContainer"
git push
