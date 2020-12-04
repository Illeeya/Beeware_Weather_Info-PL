import toga as t
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from urllib import request
from json import loads

class PogodaInfo(t.App):

    def startup(self):
        
        main_box = t.Box(style=Pack(direction= COLUMN))

        url = "https://danepubliczne.imgw.pl/api/data/synop"

        CITIES = []

        try: 
            response_pogoda = request.urlopen(url).read()
        except ConnectionError:
            err_msg = "There was a connection error."
            error_lbl = t.Label(err_msg)
            error_lbl.style.update(padding = 30)
            main_box.add(error_lbl)
        except Exception as e:    
            err_msg = f"An error occured. Error type: {type(e)}"
            error_lbl = t.Label(err_msg)
            error_lbl.style.update(padding = 30)
            main_box.add(error_lbl)
        else:

            response_pogoda = response_pogoda.decode()

            response_pogoda = loads(response_pogoda)

            #FUNCS

            def wlbl_fill(data_pomiaru, godzina_pomiaru, suma_opadu, predkosc_wiatru, temperatura):

                wlbl_001.text = f"\U0001F30C POGODA \U0001F30C"
                brk_003.text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
                wlbl_002.text =f"{data_pomiaru}    {godzina_pomiaru}:00"  
                
                wlbl_101.text = f"\U0001F327"
                wlbl_102.text = f"Opady"
                wlbl_103.text = f"{suma_opadu}"
                wlbl_104.text = f"mm"

                wlbl_201.text = f"\U0001F32A"
                wlbl_202.text = f"Wiatr"
                wlbl_203.text = f"{predkosc_wiatru}"
                wlbl_204.text = f"km/h"

                wlbl_301.text = f"\U0001F321"
                wlbl_302.text = f"Temperatura"
                wlbl_303.text = f"{temperatura}"
                wlbl_304.text = f"C"


            def wlbl_data(city_name, rsp = response_pogoda):
                for row in rsp:
                    if row["stacja"] == city_name:
                        response = row
                        break
                data_pomiaru = response['data_pomiaru']
                godzina_pomiaru = response['godzina_pomiaru']

                suma_opadu = float(response['suma_opadu'])
                predkosc_wiatru = float(response['predkosc_wiatru'])

                temperatura = float(response['temperatura'])
                wlbl_fill(data_pomiaru, godzina_pomiaru, suma_opadu, predkosc_wiatru, temperatura)
                 

            def get_selection(widget=None, city=None):
                if widget:
                    wlbl_data(widget.value)
                if city:
                    wlbl_data(city)

            #------------------------------------------------------------------------------------------------
            #DATA
            
            for row in response_pogoda:
                CITIES.append(row['stacja'])

 
            #------------------------------------------------------------------------------------------------
            #BOXES
            weather_box = t.Box(style=Pack(direction= COLUMN, padding = 10))

               
                #WEATHER BOX
                    #City Selector
            csb  = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
                    #Title
            wb01 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            brk3 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            wb02 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
                    #Opady, Wiatr, Temperatura
            wb10 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
            wb20 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
            wb30 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))

            #------------------------------------------------------------------------------------------------
            #ELEMENTS
                
                #WEATHER BOX
            city_select = t.Selection(items=CITIES, on_select=get_selection)
                    #Title
            wlbl_001 = t.Label('',     style=Pack(width = 400, font_size = 15, font_weight = 'bold', text_align = 'left'))
            brk_003  = t.Label('',     style=Pack(width = 400, font_size = 12, text_align = 'left'))
            wlbl_002 = t.Label('',     style=Pack(width = 300, font_size = 15, font_weight = 'bold', text_align = 'left'))
                    
                    #Opady
            wlbl_101 = t.Label('',     style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            wlbl_102 = t.Label('',     style=Pack(width = 125, font_size = 12, text_align = 'left'))
            wlbl_103 = t.Label('',     style=Pack(width = 100, font_size = 12, text_align = 'right'))
            wlbl_104 = t.Label('',     style=Pack(width = 50,  font_size = 12, text_align = 'right'))
                    
                    #Wiatr
            wlbl_201 = t.Label('',     style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            wlbl_202 = t.Label('',     style=Pack(width = 125, font_size = 12, text_align = 'left'))
            wlbl_203 = t.Label('',     style=Pack(width = 100, font_size = 12, text_align = 'right'))
            wlbl_204 = t.Label('',     style=Pack(width = 50,  font_size = 12, text_align = 'right'))
                    
                    #Temperatura
            wlbl_301 = t.Label('',     style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            wlbl_302 = t.Label('',     style=Pack(width = 125, font_size = 12, text_align = 'left'))
            wlbl_303 = t.Label('',     style=Pack(width = 100, font_size = 12, text_align = 'right'))
            wlbl_304 = t.Label('',     style=Pack(width = 50,  font_size = 12, text_align = 'right'))
                    
                    
      
        #------------------------------------------------------------------------------------------------
        # INSERTING ELEMENTS

            # Elements to boxes
                
                #Weather Box
                    # City Selector
        csb.add(city_select)
                    # Title
        wb01.add(wlbl_001)
        wb02.add(wlbl_002)
        brk3.add(brk_003)
                    # Opady
        wb10.add(wlbl_101)
        wb10.add(wlbl_102)
        wb10.add(wlbl_103)
        wb10.add(wlbl_104)
                    # Wiatr
        wb20.add(wlbl_201)
        wb20.add(wlbl_202)
        wb20.add(wlbl_203)
        wb20.add(wlbl_204)
                    # Temperatura
        wb30.add(wlbl_301)
        wb30.add(wlbl_302)
        wb30.add(wlbl_303)
        wb30.add(wlbl_304)


            # Boxes to boxes
        

        weather_box.add(csb)
        weather_box.add(wb01)
        weather_box.add(wb02)
        weather_box.add(brk3)
        weather_box.add(wb10)
        weather_box.add(wb20)
        weather_box.add(wb30)

            # Boxes to main
        main_box.add(weather_box)

        #------------------------------------------------------------------------------------------------
        get_selection(city = 'Białystok')
        self.main_window = t.MainWindow(title='PogodaInfo')
        self.main_window.size = (400, 350)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return PogodaInfo()
