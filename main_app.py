from kivy.app import App

from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from instructions import * 
from ruffier import *

P1 = 0
P2 = 0
P3 = 0

user_age = 0

class FirstScr(Screen):
    def __init__(self, name='one'):
        super().__init__(name=name)
    #Manual  
        man_lab = Label(text=txt_instruction)
        man_lay = BoxLayout()
        
        man_lay.add_widget(man_lab)
    

    #Labels 
        name_lab = Label(text="Имя", size_hint=(1,0.1))
        age_lab = Label(text="Возраст", markup = True, size_hint=(1,0.1))
        lab_lay = BoxLayout()

        lab_lay.add_widget(name_lab)
        lab_lay.add_widget(age_lab)


    #TextInput
        self.user_name = TextInput(multiline=False)
        self.age = TextInput(multiline=False)
        input_lay = BoxLayout()
        
        input_lay.add_widget(self.user_name)
        input_lay.add_widget(self.age)
    
    
    #Buttons
        nex = Button(text="next", size_hint=(1, 0.5))
        nex.on_press = self.next
        back = Button(text="back", size_hint=(1, 0.5))
        nb_lay = BoxLayout()
         
        nb_lay.add_widget(back)
        nb_lay.add_widget(nex)
    
   
    #GlobalLayer
        LayGlob = BoxLayout(orientation="vertical")
        
        LayGlob.add_widget(man_lay)
        LayGlob.add_widget(lab_lay)
        LayGlob.add_widget(input_lay)
        LayGlob.add_widget(nb_lay)

        self.add_widget(LayGlob)



    def next(self):

        global user_name
        user_name = self.user_name.text
        
        global user_age
        user_age = int(self.age.text)
        self.manager.transition.direction = 'left' 
        self.manager.current = 'two'

class SORRY(Screen):
    def __init__(self, name='sorry'):
        super().__init__(name=name)
        label = Label(text= "Извините, подсчёт работает только для людей с возрастом от 8 до 18")
        self.add_widget(label)



class SecondScr(Screen): 
    def __init__(self, name='two'):
        super().__init__(name=name)
    #Manual  
        man_lab = Label(text=txt_test1)
        man_lay = BoxLayout()
        
        man_lay.add_widget(man_lab)
    

    #TextInput
        self.result = TextInput(multiline=False)
        input_lay = BoxLayout()
        
        input_lay.add_widget(self.result)
    
    
    #Buttons
        nex = Button(text="next", size_hint=(1, 0.5))
        nex.on_press = self.next
        back = Button(text="back", size_hint=(1, 0.5))
        back.on_press = self.back
        nb_lay = BoxLayout()
         
        nb_lay.add_widget(back)
        nb_lay.add_widget(nex)
    
   
    #GlobalLayer
        LayGlob = BoxLayout(orientation="vertical")
        
        LayGlob.add_widget(man_lay)
        LayGlob.add_widget(input_lay)
        LayGlob.add_widget(nb_lay)

        self.add_widget(LayGlob)



    def next(self):
        global P1
        P1 = int(self.result.text)

        self.manager.transition.direction = 'left' 
        self.manager.current = 'three'
    
    def back(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'one'

class ThirdScr(Screen):
    def __init__(self, name='three'): 
        super().__init__(name=name)
    #Manual  
        man_lab = Label(text=txt_test2)
        man_lay = BoxLayout()
        
        man_lay.add_widget(man_lab)
    

    #Buttons
        nex = Button(text="next", size_hint=(1, 0.5))
        nex.on_press = self.next
        back = Button(text="back", size_hint=(1, 0.5))
        back.on_press = self.back
        nb_lay = BoxLayout()
         
        nb_lay.add_widget(back)
        nb_lay.add_widget(nex)
    
   
    #GlobalLayer
        LayGlob = BoxLayout(orientation="vertical")
        
        LayGlob.add_widget(man_lay)
        LayGlob.add_widget(nb_lay)

        self.add_widget(LayGlob)



    def next(self):
        self.manager.transition.direction = 'left'  
        self.manager.current = 'four'
    
    def back(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'two'

class FourthScr(Screen): 
    def __init__(self, name='four'):
        super().__init__(name=name) 
    #Manual  
        man_lab = Label(text=txt_test3)
        man_lay = BoxLayout()
        
        man_lay.add_widget(man_lab)
    

    #Labels 
        name_lab = Label(text="Первый резултат", size_hint=(1,0.1))
        age_lab = Label(text="Второй результат", markup = True, size_hint=(1,0.1))
        lab_lay = BoxLayout()

        lab_lay.add_widget(name_lab)
        lab_lay.add_widget(age_lab)


    #TextInput
        self.result_one = TextInput(multiline=False)
        self.result_two = TextInput(multiline=False)
        input_lay = BoxLayout()
        
        input_lay.add_widget(self.result_one)
        input_lay.add_widget(self.result_two)
    
    
    #Buttons
        nex = Button(text="next", size_hint=(1, 0.5))
        nex.on_press = self.next
        back = Button(text="back", size_hint=(1, 0.5))
        nb_lay = BoxLayout()
         
        nb_lay.add_widget(back)
        nb_lay.add_widget(nex)
    
   
    #GlobalLayer
        LayGlob = BoxLayout(orientation="vertical")
        
        LayGlob.add_widget(man_lay)
        LayGlob.add_widget(lab_lay)
        LayGlob.add_widget(input_lay)
        LayGlob.add_widget(nb_lay)

        self.add_widget(LayGlob)



    def next(self):
        global P2
        P2 = int(self.result_one.text)
        global P3
        P3 = int(self.result_two.text)

        self.manager.transition.direction = 'left' 
        self.manager.current = 'five'
        print(user_age)
    def back(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'three'


class FithScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        self.label = Label(text='')
        self.add_widget(self.label)
        
        self.on_enter = self.before
        
    def before(self):
        print(P1,P2,P3)
        ruffier_index(P1,P2,P3)

        ruff_result = ruffier_result(ruffier_index(P1,P2,P3), neud_level(user_age))

        self.label.text = user_name + '\n' + txt_index + str(ruffier_index(P1,P2,P3)) + '\n' + txt_workheart + txt_res[ruff_result]





class MyApp(App): 
    def build(self):
        sm = ScreenManager() 
        sm.add_widget(FirstScr()) 
        sm.add_widget(SecondScr()) 
        sm.add_widget(ThirdScr()) 
        sm.add_widget(FourthScr()) 
        sm.add_widget(FithScr()) 
        return sm

app = MyApp() 
app.run()


