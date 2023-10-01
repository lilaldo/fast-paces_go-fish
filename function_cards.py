import random


class Visual_card():
    def __init__(self, symbols):
        self.symbols = symbols

    def visualace(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|A        |
|         |
|    {symbol_placement}    |
|         |
|         |
|________∀|""")

    def visual2(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|2        |
|    {symbol_placement}    |  
|         |
|         |  
|    {symbol_placement}    |
|________↊|""")

    def visual3(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|3        |
|    {symbol_placement}    |
|    {symbol_placement}    |
|    {symbol_placement}    |
|         |
|________↋|""")

    def visual4(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|4        |
|  {symbol_placement}   {symbol_placement}  |  
|         |
|         |  
|  {symbol_placement}   {symbol_placement}  |
|________4|""")

    def visual5(self):
        symbol_placement = random.choice(self.symbols)
        print(f""" 
 _________
|5 {symbol_placement}   {symbol_placement}  |
|         |  
|    {symbol_placement}    |
|         |  
|  {symbol_placement}   {symbol_placement}  |
|________5|""")

    def visual6(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|6 {symbol_placement}   {symbol_placement}  |
|         |  
|  {symbol_placement}   {symbol_placement}  |
|         |  
|  {symbol_placement}   {symbol_placement}  |
|________9|""")

    def visual7(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|7        |
|  {symbol_placement}   {symbol_placement}  |  
|    {symbol_placement}    |
|  {symbol_placement}   {symbol_placement}  |  
|  {symbol_placement}   {symbol_placement}  |
|________𝘓|""")

    def visual8(self):
        symbol_placement = random.choice(self.symbols)
        print(f""" 
 _________
|8        |
|  {symbol_placement}   {symbol_placement}  |  
|  {symbol_placement}   {symbol_placement}  |
|  {symbol_placement}   {symbol_placement}  |  
|  {symbol_placement}   {symbol_placement}  |
|________8|""")

    def visual9(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|9 {symbol_placement}   {symbol_placement}  |
|    {symbol_placement}    |  
|  {symbol_placement}   {symbol_placement}  |
|  {symbol_placement}   {symbol_placement}  |  
|  {symbol_placement}   {symbol_placement}  |
|________6|""")

    def visual10(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|10{symbol_placement}   {symbol_placement}  |
|    {symbol_placement}    |  
|  {symbol_placement}   {symbol_placement}  |
|  {symbol_placement}   {symbol_placement}  |  
|    {symbol_placement}    |
|__{symbol_placement}___{symbol_placement}0I|""")

    def visualjacks(self):
        symbol_placement = random.choice(self.symbols)
        print(f""" 
 _________
|J{symbol_placement}       |
|         |  
|    J    |
|         |  
|         |
|_______{symbol_placement}J|""")

    def visualqueen(self):
        symbol_placement = random.choice(self.symbols)
        print(f"""
 _________
|       {symbol_placement}Q|
|         |  
|    Q    |
|         |  
|         |
|Q{symbol_placement}_______|""")

    def visualking(self):
        symbol_placement = random.choice(self.symbols)
        print(f""" 
 _________
|K{symbol_placement}     {symbol_placement}K|
|         |  
|    K{symbol_placement}   |
|         |  
|         |
|K{symbol_placement}_____{symbol_placement}K|""")


# SAVE FOR LATER - necessary code for print - SAVE FOR LATER
#visual_card = Visual_card(['♥', '♦', '♣', '♠'])
#Visual_card.visualking(self=visual_card)
