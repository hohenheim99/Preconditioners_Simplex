# Primero, importamos las bibliotecas necesarias
from tensorflow import keras
import numpy as np
 
# Definimos una función para generar el conjunto de datos de entrenamiento
def generate_A(n):
  A=np.random.randint(100,size=(2,2))

def generate_B(n):
  B=np.random.randint(100,size=(2,2))

def generate_X(n):
  C=np.random.randint(100,size=(2,2))

 

# Primero, importamos la clase GridSearchCV
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier

# Generamos el conjunto de datos de entrenamiento
X_train, Y_train = generate_dataset(10000)

# Creamos la función que devuelve el modelo
model = keras.Sequential()
model.add(keras.layers.Dense(32, input_shape=(4,)))
model.add(keras.layers.Dense(64,activation="tanh"))
model.add(keras.layers.Dense(4))
model.add(keras.layers.Reshape((2,2)))
model.compile(loss='mean_absolute_error', optimizer='adam')

# Entrenamos la red
model.fit(X_train, Y_train, epochs=20)

"""Para comparar el resultado de la red neuronal con el valor esperado de la inversa de una matriz, puedes utilizar la función predict de Keras para obtener la predicción de la red para una matriz dada y luego compararla con el valor esperado utilizando alguna métrica de error. Por ejemplo:"""

