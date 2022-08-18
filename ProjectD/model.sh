#! usr/bin/bash
echo Hello Model-World

echo const unsigned char model[] = { > backend/model.h
cat modelTFLite | xxd -i      >> backend/model.h
echo "};" >> backend/model.h


echo const unsigned char model[] = { > model.h
cat modelTFLite | xxd -i      >> model.h
echo "};" >> model.h

echo Python-code converted to C++ Successfully!
echo Done!
