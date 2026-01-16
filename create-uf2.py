#!/usr/bin/python3

# Adds PlatformIO post-processing to convert hex files to uf2 files

Import("env")

# Hook into the build process to create UF2 after hex is built
env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.hex",
    env.VerboseAction(" ".join([
        '"$PYTHONEXE"',
        '"$PROJECT_DIR/bin/uf2conv/uf2conv.py"',
        '-f', '0xADA52840',
        '-c', '"$BUILD_DIR/${PROGNAME}.hex"',
        '-o', '"$BUILD_DIR/${PROGNAME}.uf2"'
    ]), "Creating UF2 file")
)