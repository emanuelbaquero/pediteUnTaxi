import pandas as pd 
import streamlit as st




import smtplib 
from email.mime.text import MIMEText 



conectado=1
if conectado==1:
	emisor = "baqueroemanuel@gmail.com" 
	receptor = "andrea68segovia@gmail.com"     
	# Nos conectamos al servidor SMTP de Gmail 

	serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
	serverSMTP.ehlo() 
	serverSMTP.starttls() 
	serverSMTP.ehlo() 
	serverSMTP.login(emisor,"qgxcghstbdytzccc")
conectado=0




st.markdown('<style>.st-bm{padding-top:7%;background:#ffee3a;}</style>', unsafe_allow_html=True)



st.markdown('<style>div.block-container{background:white;opacity:.98;text-align:center;}</style>', unsafe_allow_html=True)





st.markdown('<style>section.main{background-size: cover;background-image: url(https://p4.wallpaperbetter.com/wallpaper/929/1017/70/city-lights-bokeh-lights-blurred-blurry-wallpaper-preview.jpg);}</style>', unsafe_allow_html=True)


#st.markdown('<style>section.main{background:#c8cc7d}</style>', unsafe_allow_html=True)




 










st.write(
      '<h1 class="titulo">PEDI UN TAXI...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h1.titulo{color: #323404;margin-bottom:0;padding:0;text-align:center;}h1.titulo:hover{color:#ffee3a}</style>', unsafe_allow_html=True)






st.write(
      '<h3 class="nombre_completo">Ingresa tu Nombre para identificarte...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h3.nombre_completo{color: #323404;margin:0;padding:0;text-align:center;}</style>', unsafe_allow_html=True)

var_nombre_completo = st.text_input(' ')



st.write(
      '<h3 class="numero_contacto">Ingresa tu Numero de Telefono o Celular de Contacto...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h3.numero_contacto{color: #323404;margin:0;padding:0;text-align:center;}</style>', unsafe_allow_html=True)


var_numero_contacto = st.text_input('  ')



st.write(
      '<h3 class="parte_de">Escriba la direccion completa desde donde sale (SALIDA)...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h3.parte_de{margin:0;padding:0;text-align:center;}</style>', unsafe_allow_html=True)



var_salida = st.text_input('      ')



st.write(
      '<h3 class="parte_de">Escriba la direccion donde quiere ir (DESTINO)...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h3.parte_de{margin:0;padding:0;text-align:center;}</style>', unsafe_allow_html=True)

var_destino = st.text_input('    ')





# Configuracion del mail 
mensaje = MIMEText("Se ha registrado un nuevo Pasajero\n\n: "+var_nombre_completo+"\n\nContacto: "+var_numero_contacto+"\n\nSalida: "+var_salida+"\n\nDestino: "+var_destino) 
mensaje['From']=emisor 
mensaje['To']=receptor 
mensaje['Subject']="Nuevo Pasajero TAXI"     


if st.button('Hacer Pedido de Taxi'):
	if var_numero_contacto != '':

			st.write('<h3 class="pedido_confirmado">Buenisimo, se ha cargado su pedido, Espere a ser contactado</h3>',unsafe_allow_html=True)
			st.	markdown('<style>h3.pedido_confirmado{color:black;font-size=3em;margin:0;padding:0;}</style>', unsafe_allow_html=True)
	
			# Enviamos el mensaje 
			serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
			# Cerramos la conexion 
			serverSMTP.close()
	else:
		st.write(
      	'<h3 class="no_ingreso_telefono">Error, Numero de telefono no ingresado...</h3>',unsafe_allow_html=True)
		st.markdown('<style>h3.no_ingreso_telefono{margin:0;padding:0;}</style>', unsafe_allow_html=True)

