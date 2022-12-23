```python

@task()
# def init(**kwargs):
#     print("INFO >>>>> INIT CALL INITIATED ⚙️ ⚙️ ⚙️")
#     print(type(config))
#     trigger_payload = kwargs.get('params', {})
#     envs = Variable.get("enven_planning", deserialize_json=True)
#     if trigger_payload:
#
#         c = trigger_payload.get("groupings", "change_one_it")
#         parsed_envs = {
#             "sftp_source_directory": c
#         }
#         try:
#             external_params = Variable.get("enven_planning_external_params", deserialize_json=True)
#             Variable.set(key="enven_planning_external_params", value=json.dumps(parsed_envs))
#         except Exception as e:
#             print(e)
#             enven_planning_external_params = Variable(key="enven_planning_external_params", val=json.dumps(parsed_envs))
#             session = Session()
#             session.add(enven_planning_external_params)
#             session.commit()
#
#         print(f"INFO >>>>> parserd envs after loader = {str(parsed)}")
#     print(f"INFO >>>>> configs parsed {config}")
```
