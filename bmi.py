class BMI:
    def __init__(self, height, weight):
        # インスタンス変数として計算式の結果をself.valueに代入
        self.value = weight / (height ** 2)
        # initメソッドでtanaka_bmiのオブジェクトができる

        if not (10 <= self.value <= 40):
            raise ValueError("BMIが正常値の範囲を超えています")
    
    def __str__(self):
        return f"{self.value:.2f}"
    # オブジェクトをprint()やformat()で呼び出した場合に文字列を返すためのメソッド 返り値はstring(文字列)である必要

# ここより上はただの設計図

# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0) # 引数 #メソッドに対して、入れているということ
sasami_bmi = BMI(height=1.58, weight=80.0) # スペースは不要
bob_bmi = BMI(height=1.70, weight=75000.0)

print(tanaka_bmi)
print(sasami_bmi)
print("error")
print(bob_bmi)
