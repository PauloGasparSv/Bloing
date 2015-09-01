def main():
	blank_file = open("../Assets/Stages/test_stage/inimigos.stage",'w');
	for i in range(0,15):
		if(i < 4):
			blank_file.write("C;"+str(660+i*60)+";"+str(560)+" ");
			blank_file.write("C;"+str(1555+i*60)+";"+str(250)+" ");
			blank_file.write("C;"+str(2400+i*60)+";"+str(360)+" ");
		blank_file.write("C;"+str(1960+i*60)+";"+str(130)+" ");
		blank_file.write("C;"+str(1960+i*60)+";"+str(80)+" ");
		blank_file.write("C;"+str(-1800+i*60)+";"+str(570)+" ");
		blank_file.write("C;"+str(-1800+i*60)+";"+str(530)+" ");
		

	blank_file.close();

if __name__ == "__main__":
	main();