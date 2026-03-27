Methodology: CAD Reconstruction via Parametric Modeling Pipeline

Each component of the RetroPad assembly is reconstructed through individual Python scripts using the build123d framework. The workflow is structured to ensure accurate geometry recreation, modular development, and reproducible outputs.

Per-Component Scripts
Each part is implemented as a dedicated Python script that defines the geometry using parametric modeling operations such as sketching, extrusion, boolean operations, and filleting. The reference STL files are used to guide dimensions and geometry. Each script outputs a corresponding STEP or STL file, ensuring that every component is treated as an independent and self-contained unit.

Geometry Reconstruction Strategy
The reconstruction process involves analyzing the reference STL geometry and decomposing it into fundamental primitives. Dimensions and features are iteratively refined to closely match the original mesh. Special attention is given to preserving symmetry, maintaining critical design features, and ensuring the resulting model is a valid solid.

Assembly Script
A separate assembly script imports all reconstructed components and positions them using spatial transformations. The individual parts are combined into a single assembly structure representing the complete RetroPad case. The final assembly is exported as a unified STEP file and, where required, converted into STL format for downstream use.

File Embedding via Base64 Encoding
To ensure portability and reproducibility, CAD files are embedded directly into Python scripts using base64 encoding. Each generator script stores the encoded representation of a file, decodes it during execution, and regenerates the original STEP or STL file. This approach removes the need for external file dependencies and guarantees consistent outputs across different environments.

Validation and Accuracy Check
Model accuracy is evaluated by comparing the volume of the reconstructed geometry with the corresponding STL reference. The volume difference is measured and verified to be within an acceptable tolerance. Due to the mesh-based nature of STL files, exact boolean comparison is not always reliable; therefore, volume comparison is used as the primary validation metric.

Dependency Management
All required dependencies, including build123d and supporting CAD libraries, are defined in a requirements.txt file. This ensures that the project environment can be reproduced consistently without manual setup.
