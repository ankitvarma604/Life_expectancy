from flask import Flask, request, app, render_template
import pickle

class pred:
    def __init__(self,val):
        self.val = val

    def predict_life(self):
        model = pickle.load(open("Life_Expectancy.sav", "rb"))
        result = int(model.predict(self.val)[0])
        return result