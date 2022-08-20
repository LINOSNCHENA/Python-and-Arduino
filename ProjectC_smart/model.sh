#! usr/bin/bash
echo ====================|A|============|CC\CC|==========
echo Hello World
echo Done!

echo const unsigned char model[] = { > backend3/model.h
cat modelTFLite | xxd -i      >> backend3/model.h
echo };       >> backend3/model.h

echo Python-code converted to C++ Successfully!
echo Done!
echo =====================|B|===========|C\CCC|===========
