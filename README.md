# LED-Display
30x20 pixels LED Display made from a LED strip (check this video https://youtu.be/sfm653IPXeM).

1 - Make a LED display from a WS2812B strip (or another addressable LED strip).
	I used two 5m strips, which have 60 LEDS per meter, for a total of 600 LEDS (30 columns x 20 rows).
	Check the Manual do Mundo video (https://youtu.be/sfm653IPXeM) to get the DIY instructions.
2 - Generate the images you want to display using Photoshop (or another software you like).
	You can use the template file "30x20.psd" as a reference. Try your best pixelart skills :D
3 - Export your image as an 30x20 pixels (or your display resolution) PNG file, no transparency.
4 - Run the python file "pixelcolor_extractor.py" (change the variable "filename" to point to your file) to convert that image into Arduino codes (the output is a text file in the "txts" folder).
5 - Paste that code into the "Arduino/LED-Display/LED-Display.ino" file, under a function (check the file for examples).
6 - Setup the parameters of "Arduino/LED-Display/LED-Display.ino" file (check the file for instructions).
7 - Compile the code and upload to your Arduino.
8 - If you want to make an animation, use the "Arduino/DinoGame.ino" as a guide.
9 - Have fun!
10 - Send me feedback and your project pictures.

:D

Important
	Arduino doesn't have enough internal memory to store many images. If you are getting full memory error when compiling, you have to remove some images from the code.
	If you can, use an Arduino Mega which can handle much more images than Arduino Uno. I don't know if Arduino Nano have the minimum to run this project.
	I intended to write a code which stored the images inside arrays, but the Arduino Uno I was using didn't have enough memory to compile that code.
	So I decided to store the code lines which set each pixel color directly inside a function.
	But even so, Arduino Uno could only store some images (I think 3 or 4) each time.
	Then I obtained an Arduino Mega which have much more memory and made my life easier.


--------------------------------------

Um Monitor feito a partir de uma Fita LED (veja esse v??deo https://youtu.be/sfm653IPXeM).

1 - Construa um monitor LED a partir de uma fita WS2812B (ou alguma outra fita endere????vel).
	Eu usei duas fitas de 5m, com 60 LEDs por metro, o que d?? 600 LEDs no total (30 colunas por 20 linhas).
	Veja o v??deo do Manual do Mundo (https://youtu.be/sfm653IPXeM) com as instru????es.
2 - Gere as imagens que voc?? quiser mostrar no monitor usando Photoshop (ou outro software de imagens).
	Use o arquivo de refer??ncia "30x20.psd" para te facilitar. Capriche nas suas habilidades de pixelArt :D
3 - Exporte sua imagem como um PNG de resolu????o 30x20 (ou a mesma do seu monitor), sem transpar??ncia.
4 - Rode o arquivo de python "pixelcolor_extractor.py" (mude a vari??vel "filename" para o seu arquivo) para converter essa imagem em c??digos do Arduino (a sa??da ?? um arquivo de texto dentro da pasta "txts").
5 - Cole esse c??digo em "Arduino/LED-Display/LED-Display.ino", dentro de uma fun????o (veja o arquivo para ter exemplos).
6 - Configure os par??metros do "Arduino/LED-Display/LED-Display.ino" (veja o arquivo para instru????es).
7 - Compile o c??digo e suba para seu Arduino.
8 - Se quiser fazer uma anima????o, use o "Arduino/DinoGame" como uma refer??ncia.
8 - Divirta-se!!
9 - Me mande suas impress??es, coment??rio e fotos das suas imagens.

:D

Importante
	O Arduino n??o tem mem??ria interna suficiente para armazenar muitas imagens. Se voc?? est?? tendo um erro de mem??ria cheia ao compilar, ter?? que remover algumas imagens do c??digo.
	Se poss??vel, use um Arduino Mega, que consegue lidar com muito mais imagens do que o Arduino Uno. Eu n??o sei se o Arduino Nano d?? conta desse projeto.
	Minha ideia era escrever um c??digo que armazenava as imagens dentro de arrays, mas o Arduino Uno que eu estava usando n??o tinha mem??ria suficiente para compilar essas instru????es.
	Ent??o eu decidi armazenar diretamente os comandos que trocam as cores de cada pixel diretamente dentro de uma fun????o.
	Mesmo assim, o Arduino Uno s?? conseguia armazenar poucas imagens (acho que umas 3 ou 4) por vez.
	Da?? eu consegui um Arduino Mega e minha vida ficou bem mais f??cil hehe. Recomendo que use um Mega tamb??m.

