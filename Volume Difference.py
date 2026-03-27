from build123d import *

stl_model = import_stl("assembly.stl")
my_model = import_step("assembly.step")

print("STL Volume:", stl_model.volume)
print("My Model Volume:", my_model.volume)

diff = abs(stl_model.volume - my_model.volume)
print("Volume Difference:", diff)

if diff < 1:
    print("✅ Volume match within tolerance")
else:
    print("❌ Volume mismatch")