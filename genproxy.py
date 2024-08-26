#V1.0
Z='Masukkan interface: '
Y='y'
X='Gunakan custom interface? (y/n): '
W='Masukkan UUID: '
V='Masukkan bugs (pisahkan dengan koma atau nama file .txt): '
U='Masukkan server: '
T='/trojan'
R='4'
Q='3'
P='Pilihan tidak valid.'
O='2'
N='1'
M='Pilih opsi: '
L='/vless'
K='/vmess'
G='Masukkan GRPC service name: '
F='\n'
C=None
B=print
A=input
import os
def D(bugs_input):
	A=bugs_input
	if os.path.isfile(A):
		with open(A,'r')as C:B=C.read().splitlines()
	else:B=A.split(',')
	return[A.strip()for A in B if A.strip()]
def E(bug):
	B='.';A=bug
	if A.replace(B,'').isdigit():C=A.split(B);D=f"{C[-2]}-{C[-1]}"
	else:D=A.split(B)[0]
	return D
def a(server,bugs,uuid,path=K,interface=C):
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
def b(server,bugs,uuid,path=K,interface=C):
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
def c(server,bugs,uuid,path=K,interface=C):
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
def d(server,bugs,uuid,path=K,interface=C):
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
def e(server,bugs,uuid,grpc_name,interface=C):
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
def f(server,bugs,uuid,grpc_name,interface=C):
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
def g(server,bugs,uuid,path=T,interface=C):
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
def h(server,bugs,uuid,path=T,interface=C):
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
def i(server,bugs,uuid,grpc_name,interface=C):
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
def j(server,bugs,uuid,grpc_name,interface=C):
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
def k(server,bugs,uuid,path=L,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-WS-TLS-{I}
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
def l(server,bugs,uuid,path=L,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-WS-NTLS-{I}
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
def m(server,bugs,uuid,path=L,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-SNI-TLS-{I}
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
def n(server,bugs,uuid,path=L,interface=C):
	B=interface;C=[];H=D(bugs)
	for A in H:
		I=E(A);G=f"""
- name: V-SNI-NTLS-{I}
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
def p(server,bugs,uuid,interface=C):
	A=interface;B=[];H=D(bugs)
	for C in H:
		I=E(C);G=f"""
- name: V-XTLS-{I}
  type: vless
  server: {C}
  port: 443
  uuid: {uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  servername: {server}
  network: tcp"""
		if A:G+=f"\n  interface-name: {A}"
		B.append(G.strip())
	return F.join(B)
def H():
	D=A(U);E=A(V);F=A(W);L=A('Masukkan path (default /vmess): ')or K;g=A(X).strip().lower()==Y;H=A(Z)if g else C;B('1. Generate Vmess CDN TLS/443');B('2. Generate Vmess CDN NTLS/80');B('3. Generate Vmess SNI TLS/443');B('4. Generate Vmess SNI NTLS/80');B('5. Generate Vmess GRPC CDN/443');B('6. Generate Vmess GRPC SNI/443');I=A(M)
	if I==N:J=a(D,E,F,L,H)
	elif I==O:J=b(D,E,F,L,H)
	elif I==Q:J=c(D,E,F,L,H)
	elif I==R:J=d(D,E,F,L,H)
	elif I=='5':T=A(G);J=e(D,E,F,T,H)
	elif I=='6':T=A(G);J=f(D,E,F,T,H)
	else:B(P);return
	S(J)
def I():
	D=A(U);E=A(V);F=A(W);L=A('Masukkan path (default /trojan): ')or T;a=A(X).strip().lower()==Y;H=A(Z)if a else C;B('1. Generate Trojan WS SNI/443');B('2. Generate Trojan WS CDN/443');B('3. Generate Trojan GRPC SNI/443');B('4. Generate Trojan GRPC CDN/443');I=A(M)
	if I==N:J=g(D,E,F,L,H)
	elif I==O:J=h(D,E,F,L,H)
	elif I==Q:K=A(G);J=i(D,E,F,K,H)
	elif I==R:K=A(G);J=j(D,E,F,K,H)
	else:B(P);return
	S(J)
def J():
	D=A(U);E=A(V);F=A(W);K=A('Masukkan path (default /vless): ')or L;a=A(X).strip().lower()==Y;H=A(Z)if a else C;B('1. Generate Vless WS TLS/443');B('2. Generate Vless WS NTLS/80');B('3. Generate Vless SNI TLS/443');B('4. Generate Vless SNI NTLS/80');B('5. Generate Vless GRPC SNI/443');B('6. Generate Vless GRPC CDN/443');I=A(M)
	if I==N:J=k(D,E,F,K,H)
	elif I==O:J=l(D,E,F,K,H)
	elif I==Q:J=m(D,E,F,K,H)
	elif I==R:J=n(D,E,F,K,H)
	elif I=='5':T=A(G);J=generate_vless_grpc_sni(D,E,F,T,H)
	elif I=='6':T=A(G);J=generate_vless_grpc_cdn(D,E,F,T,H)
	else:B(P);return
	S(J)
def S(config):
	C=config;B('1. Print konfigurasi');B('2. Simpan ke file');D=A(M)
	if D==N:B(C)
	elif D==O:
		E=A('Masukkan nama file: ')
		with open(E,'w')as F:F.write(C)
		B(f"Konfigurasi disimpan ke {E}")
	else:B(P)
def o():
	try:
		while True:
			B('1. Generate Vmess');B('2. Generate Trojan');B('3. Generate Vless');B('4. Keluar');C=A(M)
			if C==N:H()
			elif C==O:I()
			elif C==Q:J()
			elif C==R:break
			else:B(P)
	except KeyboardInterrupt:B('\nTerimakasih sudah menggunakan script ini')
if __name__=='__main__':o()
