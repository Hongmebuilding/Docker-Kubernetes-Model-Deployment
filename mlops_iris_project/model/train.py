from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1️⃣ 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 2️⃣ 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 3️⃣ 모델 저장
joblib.dump(model, "model/model.pkl")
print("🎯 모델 학습 완료! 'model.pkl' 파일로 저장되었습니다.")
