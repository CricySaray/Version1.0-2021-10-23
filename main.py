import sys
import QtDisigner实验
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
'''
if __name__ == '__main__':
	# 创建QApplication类的实例
	app = QApplication(sys.argv)
	# 创建一个窗口
	w = QWidget()
	# 设置窗口尺寸
	w.resize(400, 200)
	# 移动窗口
	w.move(300, 300)
	
	# 设置窗口的标题
	w.setWindowTitle('第一个基于PyQt5的桌面应用')
	# 显示窗口
	w.show()
'''
if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWindows = QMainWindow()
	ui = QtDisigner实验.Ui_MainWindow()
	# 向主窗口上添加控件
	ui.setupUi(mainWindows)
	mainWindows.show()
	sys.exit(app.exec_())
