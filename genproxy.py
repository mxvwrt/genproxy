Z='Masukkan interface: '
Y='Gunakan custom interface? (y/n): '
X='Masukkan UUID: '
W='Masukkan bugs (pisahkan dengan koma atau nama file .txt): '
V='Masukkan server: '
J=open
S='4'
R='3'
I='/trojan'
Q='y'
P='Pilihan tidak valid.'
O='2'
N='1'
M='Pilih opsi: '
L='Masukkan GRPC service name: '
H='/vless'
G='/vmess'
F='\n'
C=None
B=print
A=input
import requests,os,subprocess as K,sys
try:import requests
except ImportError:import pip;pip.main(['install','requests'])
__version__='0.1'
T='https://raw.githubusercontent.com/mxvwrt/genproxy/main/version'
a='https://raw.githubusercontent.com/mxvwrt/genproxy/main/genproxy.py'
def b(url):
	A=requests.get(url)
	if A.status_code==200:return A.text.strip()
	else:return
def c(local_version,latest_version):return local_version<latest_version
def d():
	A='updater.py'
	if not os.path.isfile(A):
		B='\nimport requests\nupdate_url = "https://raw.githubusercontent.com/mxvwrt/genproxy/main/genproxy.py"\ndef download_update(update_url):\n    response = requests.get(update_url)\n    if response.status_code == 200:\n        with open("genproxy.py", "w") as file:\n            file.write(response.text)\n        print("Update berhasil diunduh dan genproxy.py diperbarui.")\n    else:\n        print("Gagal mendownload update.")\ndef main():\n    download_update(update_url)\nif __name__ == "__main__":\n    main()\n'
		with J(A,'w')as C:C.write(B)
def e():
	C=b(T)
	if C:
		if c(__version__,C):
			B(f"Versi terbaru tersedia: {C}");D=A('Apakah Anda ingin melakukan update? (y/n): ').strip().lower()
			if D==Q:B('Memulai proses pembaruan...');d(a);K.run([sys.executable,'update.py'],check=True);B('Update selesai. Silahkan jalankan ulang Program.');sys.exit()
			else:B('Update dibatalkan.')
		else:B('Anda sudah menggunakan versi terbaru.')
	else:B('Tidak dapat memeriksa versi terbaru.')
def D(bugs_input):
	A=bugs_input
	if os.path.isfile(A):
		with J(A,'r')as C:B=C.read().splitlines()
	else:B=A.split(',')
	return[A.strip()for A in B if A.strip()]
def E(bug):
	D='.';B=bug
	if B.replace(D,'').isdigit():A=B.split(D);C=f"{A[-2]}-{A[-1]}"
	else:
		A=B.split(D)
		if len(A)>1:C=f"{A[0]}-{A[1]}"
		else:C=A[0]
	return C
def f(server,bugs,uuid,path=G,interface=C):
	B=interface;A=server;C=[];I=D(bugs)
	for G in I:
		J=E(G);H=f"""
- name: V-TLS-CDN-{J}
  type: vmess
  server: {G}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  skip-cert-verify: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:H+=f"\n  interface-name: {B}"
		C.append(H.strip())
	return F.join(C)
def g(server,bugs,uuid,path=G,interface=C):
	B=interface;A=server;C=[];I=D(bugs)
	for G in I:
		J=E(G);H=f"""
- name: V-NTLS-CDN-{J}
  type: vmess
  server: {G}
  port: 80
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: false
  skip-cert-verify: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:H+=f"\n  interface-name: {B}"
		C.append(H.strip())
	return F.join(C)
def h(server,bugs,uuid,path=G,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-TLS-SNI-{I}
  type: vmess
  server: {server}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  skip-cert-verify: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def i(server,bugs,uuid,path=G,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-NTLS-SNI-{I}
  type: vmess
  server: {server}
  port: 80
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: false
  skip-cert-verify: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def j(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: V-GRPC-CDN-{I}
  server: {C}
  port: 443
  type: vmess
  uuid: {uuid}
  alterId: 0
  cipher: auto
  network: grpc
  tls: true
  servername: {server}
  skip-cert-verify: true
  grpc-opts:
    grpc-service-name: {grpc_name}"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def k(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: V-GRPC-SNI-{I}
  server: {server}
  port: 443
  type: vmess
  uuid: {uuid}
  alterId: 0
  cipher: auto
  network: grpc
  tls: true
  servername: {C}
  skip-cert-verify: true
  grpc-opts:
    grpc-service-name: {grpc_name}"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def l(server,bugs,uuid,path=I,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: T-WS-SNI-{I}
  server: {server}
  port: 443
  type: trojan
  password: {uuid}
  network: ws
  sni: {A}
  skip-cert-verify: true
  udp: true
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def m(server,bugs,uuid,path=I,interface=C):
	B=interface;A=server;C=[];I=D(bugs)
	for G in I:
		J=E(G);H=f"""
- name: T-WS-CDN-{J}
  server: {G}
  port: 443
  type: trojan
  password: {uuid}
  network: ws
  sni: {A}
  skip-cert-verify: true
  udp: true
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:H+=f"\n  interface-name: {B}"
		C.append(H.strip())
	return F.join(C)
def n(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: T-GRPC-SNI-{I}
  type: trojan
  server: {server}
  port: 443
  password: {uuid}
  udp: true
  sni: {C}
  skip-cert-verify: true
  network: grpc
  grpc-opts:
    grpc-service-name: {grpc_name}"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def o(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: T-GRPC-CDN-{I}
  type: trojan
  server: {C}
  port: 443
  password: {uuid}
  udp: true
  sni: {server}
  skip-cert-verify: true
  network: grpc
  grpc-opts:
    grpc-service-name: {grpc_name}"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def p(server,bugs,uuid,path=H,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: VL-WS-TLS-{I}
  type: vless
  server: {server}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def q(server,bugs,uuid,path=H,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: VL-WS-NTLS-{I}
  type: vless
  server: {server}
  port: 80
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: false
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def r(server,bugs,uuid,path=H,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: VL-SNI-TLS-{I}
  type: vless
  server: {server}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def s(server,bugs,uuid,path=H,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: VL-SNI-NTLS-{I}
  type: vless
  server: {server}
  port: 80
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: false
  servername: {A}
  network: ws
  ws-opts:
    path: {path}
    headers:
      Host: {A}"""
		if B:G+=f"\n  interface-name: {B}"
		C.append(G.strip())
	return F.join(C)
def t(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: VL-GRPC-SNI-{I}
  server: {server}
  port: 443
  type: vless
  uuid: {uuid}
  cipher: auto
  tls: true
  skip-cert-verify: true
  servername: {C}
  network: grpc
  grpc-opts:
  grpc-mode: gun
  grpc-service-name: {grpc_name}
  udp: true"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def u(server,bugs,uuid,grpc_name,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: VL-GRPC-CDN-{I}
  server: {C}
  port: 443
  type: vless
  uuid: {uuid}
  cipher: auto
  tls: true
  skip-cert-verify: true
  servername: {server}
  network: grpc
  grpc-opts:
  grpc-mode: gun
  grpc-service-name: {grpc_name}
  udp: true"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def v(server,bugs,uuid,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: VL-XTLS-{I}
  type: vless
  server: {server}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  servername: {C}
  network: tcp"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def w():
	T='Masukkan path (default /vmess): ';E=A(V);F=A(W);H=A(X);b=A(Y).strip().lower()==Q;I=A(Z)if b else C;B('1. Generate Vmess CDN TLS/443');B('2. Generate Vmess CDN NTLS/80');B('3. Generate Vmess SNI TLS/443');B('4. Generate Vmess SNI NTLS/80');B('5. Generate Vmess GRPC CDN/443');B('6. Generate Vmess GRPC SNI/443');J=A(M)
	if J==N:D=A(T)or G;K=f(E,F,H,D,I)
	elif J==O:D=A(T)or G;K=g(E,F,H,D,I)
	elif J==R:D=A(T)or G;K=h(E,F,H,D,I)
	elif J==S:D=A(T)or G;K=i(E,F,H,D,I)
	elif J=='5':a=A(L);K=j(E,F,H,a,I)
	elif J=='6':a=A(L);K=k(E,F,H,a,I)
	else:B(P);return
	U(K)
def x():
	a='Masukkan path (default /trojan): ';D=A(V);E=A(W);F=A(X);b=A(Y).strip().lower()==Q;G=A(Z)if b else C;B('1. Generate Trojan WS SNI/443');B('2. Generate Trojan WS CDN/443');B('3. Generate Trojan GRPC SNI/443');B('4. Generate Trojan GRPC CDN/443');H=A(M)
	if H==N:K=A(a)or I;J=l(D,E,F,K,G)
	elif H==O:K=A(a)or I;J=m(D,E,F,K,G)
	elif H==R:T=A(L);J=n(D,E,F,T,G)
	elif H==S:T=A(L);J=o(D,E,F,T,G)
	else:B(P);return
	U(J)
def y():
	T='Masukkan path (default /vless): ';D=A(V);E=A(W);F=A(X);b=A(Y).strip().lower()==Q;G=A(Z)if b else C;B('1. Generate Vless WS TLS/443');B('2. Generate Vless WS NTLS/80');B('3. Generate Vless SNI TLS/443');B('4. Generate Vless SNI NTLS/80');B('5. Generate Vless GRPC SNI/443');B('6. Generate Vless GRPC CDN/443');B('7. Generate Vless XTLS CDN/443');I=A(M)
	if I==N:J=A(T)or H;K=p(D,E,F,J,G)
	elif I==O:J=A(T)or H;K=q(D,E,F,J,G)
	elif I==R:J=A(T)or H;K=r(D,E,F,J,G)
	elif I==S:J=A(T)or H;K=s(D,E,F,J,G)
	elif I=='5':a=A(L);K=t(D,E,F,a,G)
	elif I=='6':a=A(L);K=u(D,E,F,a,G)
	elif I=='7':K=v(D,E,F,G)
	else:B(P);return
	U(K)
def U(config):
	C=config;B('1. Print konfigurasi');B('2. Simpan ke file');D=A(M)
	if D==N:B(C)
	elif D==O:
		E=A('Masukkan nama file: ')
		with J(E,'w')as F:F.write(C)
		B(f"Konfigurasi disimpan ke {E}")
	else:B(P)
def z():
	try:
		while True:
			e();B('1. Generate Vmess');B('2. Generate Trojan');B('3. Generate Vless');B('4. Keluar');C=A(M)
			if C==N:w()
			elif C==O:x()
			elif C==R:y()
			elif C==S:break
			else:B(P)
	except KeyboardInterrupt:B('\nTerimakasih sudah menggunakan script ini')
if __name__=='__main__':z()
