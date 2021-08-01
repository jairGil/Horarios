# -----------------------Stylesheet for first view
style_first = '''
QWidget{
     background-color: rgb(255, 255, 255); 
}

QPushButton{
     background-color: rgb(58, 80, 56);
     border-radius: 20px;
     font: 18pt \"Algerian\";
     color: white;
     width: 200;
     height: 40;
}

QPushButton:hover{ 
     background-color: rgb(167, 150, 77);
}

QPushButton:pressed{
     background-color: rgb(58, 80, 56); 
}

QLabel#lbl_fiuaemex{
     image: url(../view/images/fingenieria.png);
}
'''

# -----------------------Stylesheet for second view
style_second = '''
QFrame{
     background-color: rgb(255, 255, 255);
}

QFrame#frm_buttons{
     background-color: rgb(49, 68, 47);
}

QLabel{
     font: 87 12pt \"Arial\";
}

QPushButton{
    background-color: rgb(49, 68, 47);
    border: none;
    border-radius: 0px;
    font: 87 12pt \"Arial Black\";
    color: white;
    height: 50px;
}

QPushButton:hover, QPushButton:checked{
     background-color: rgb(167, 150, 77); 
}

#UA_button{
    border: 2px solid green;
    border-radius: 4px;
    background-color: white;
    padding: 4px;
}

#UA_button:checked {
    background-color: rgb(20, 130, 0);
    color: white;
}

QCheckBox{
    border: 2px solid;
    border-color: rgb(49, 68, 47);
    height: 30px;
    border-radius: 8px;
}

QCheckBox::indicator{
    margin-left: 8px;
    border: 2px solid;
    border-color: rgb(49, 68, 47);
    width: 15px;
    height: 15px;
    border-radius: 6px;
}

QCheckBox::indicator:checked{
     image: url(../view/images/checkmark.png);
}

QCheckBox::indicator:hover{
     background-color: rgb(49, 68, 47);
}

QScrollBar:vertical{
    border: none;
    width: 15px;
    margin: 15px 0;
    background-color: rgb(177, 177, 177);
}

QScrollBar::handle:vertical{
    background-color: rgb(167, 150, 77);
    min-height: 30px;
    border-radius: 7px;
}

QScrollBar::handle:vertical:pressed, QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed{
     background-color: rgb(29, 40, 28);
}

QScrollBar::sub-line:vertical{
    border: none;
    height: 15px;
    background-color: rgb(167, 150, 77);
    border-top-right-radius: 7px;
    border-top-left-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
    image: url(../view/images/sort_up.png);
}

QScrollBar::add-line:vertical{
    border: none;
    height: 15px;
    background-color: rgb(167, 150, 77);
    border-bottom-right-radius: 7px;
    border-bottom-left-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
    image: url(../view/images/sort_down.png);
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
}

QScrollBar:horizontal{
    border: none;
    height: 15px;
    margin: 0 15px;
    background-color: rgb(177, 177, 177);
}

QScrollBar::handle:horizontal{
    background-color: rgb(167, 150, 77);
    min-width: 15px;
    border-radius: 7px;
}

QScrollBar::handle:horizontal:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed{
     background-color: rgb(29, 40, 28);
}

QScrollBar::sub-line:horizontal{
    border: none;
    width: 15px;
    background-color: rgb(167, 150, 77);
    border-top-left-radius: 7px;
    border-bottom-left-radius: 7px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    image: url(../view/images/sort_left.png);
}

QScrollBar::add-line:horizontal{
    border: none;
    width: 15px;
    background-color: rgb(167, 150, 77);
    border-top-right-radius: 7px;
    border-bottom-right-radius: 7px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    image: url(../view/images/sort_right.png);
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
     background: none;
}
'''
