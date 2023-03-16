import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Paso 1: Preparación de datos
data = pd.read_csv('tu_archivo.csv')
data = data.drop(['columna_irrelevante_1', 'columna_irrelevante_2'], axis=1)
data = pd.get_dummies(data, columns=['fuente', 'ciudad'])
X = data.drop(['estado de lead'], axis=1)
y = data['estado de lead']

# Paso 2: División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Creación del modelo
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Paso 4: Evaluación del modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(f'Precisión: {precision}, Sensibilidad: {recall}, Exactitud: {accuracy}')
