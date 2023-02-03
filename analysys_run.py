#import scripts.analysys.analysys
from keras.models import load_model
import numpy as np
from keras.preprocessing.text import Tokenizer

loadmodel = load_model('./mnist-dense.hdf5')
toPredict = ['Дем’ян . Вчора сіно у Вороного згоріло, а він скаржився старшині, що','Одні казали: великого, бач, щастя запобігла — пристава з часті! І вдень не їж, і вночі не спи та все ганяй, як скажений собака, виваливши язика.','Та все ж вона йому не рівня: вона значного, хоч і зубожілого роду, інститутка']
print(loadmodel.predict((toPredict[:1])))