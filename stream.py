import pandas as pd 
import streamlit as st



st.markdown('<style>div.block-container{background:#edf19b;opacity:.9;text-align:center;}</style>', unsafe_allow_html=True)





st.markdown('<style>section.main{background-image:url(https://static.ellitoral.com/um/fotos/191877_1.jpg)}</style>', unsafe_allow_html=True)


#st.markdown('<style>section.main{background:#c8cc7d}</style>', unsafe_allow_html=True)




 










st.write(
      '<h1 class="titulo">Pedite un Taxi...</h3>',
      unsafe_allow_html=True
  )
st.markdown('<style>h1.titulo{color: #323404;margin-bottom:0;padding:0;text-align:center;}</style>', unsafe_allow_html=True)






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

hist = pd.read_csv('pedidos.csv',sep='|')
validar = (hist.telefono.astype(str).str.contains('^'+var_numero_contacto+'$',regex=True)).value_counts().shape[0]


if st.button('Hacer Pedido de Taxi'):
	if var_numero_contacto != '':
		if validar == 1:
			df_nuevos = pd.DataFrame({'nombre_completo':pd.Series(var_nombre_completo), 'telefono':pd.Series(var_numero_contacto),'salida':pd.Series(var_salida),'destino':pd.Series(var_destino)})
			df_historial = pd.read_csv('pedidos.csv',sep='|')
			df_historial = df_historial.iloc[:,1:]
			df_salida = pd.concat([df_historial,df_nuevos],axis=0)
			df_salida = df_salida.iloc[:,1:]
			df_salida.to_csv('pedidos.csv',sep='|')

			st.write('<h3 class="pedido_confirmado">Buenisimo, se ha cargado su pedido, Espere a ser contactado</h3>',unsafe_allow_html=True)
			st.	markdown('<style>h3.pedido_confirmado{color:black;font-size=3em;margin:0;padding:0;}</style>', unsafe_allow_html=True)
	
		else:
			st.write('<h3 class="no_ingreso_telefono">Ya ha cargado su pedido, Espere a ser contactado</h3>',unsafe_allow_html=True)
			st.	markdown('<style>h3.no_ingreso_telefono{margin:0;padding:0;}</style>', unsafe_allow_html=True)
	else:
		st.write(
      	'<h3 class="no_ingreso_telefono">Error, Numero de telefono no ingresado...</h3>',unsafe_allow_html=True)
		st.markdown('<style>h3.no_ingreso_telefono{margin:0;padding:0;}</style>', unsafe_allow_html=True)

