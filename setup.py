from distutils.core import setup # Need this to handle modules
import py2exe 
import pytube
import tkinter as tk
import customtkinter as ctk


setup(windows=['main.py']) # Calls setup function to indicate that we're dealing with a single console applicatio