import requests
from bs4 import BeautifulSoup

a = requests.get("https://www.reddit.com/t/nfl/")
b = requests.get("https://www.reddit.com/?feed=home")
c = requests.get("https://www.reddit.com/r/popular/")
d = requests.get("https://www.reddit.com/t/valheim/")
e = requests.get("https://www.reddit.com/t/genshin_impact/")
f = requests.get("https://www.reddit.com/t/minecraft/")
g = requests.get("https://www.reddit.com/t/pokimane/")
h = requests.get("https://www.reddit.com/t/halo_infinite/")
i = requests.get("https://www.reddit.com/t/hollow_knight_silksong/")
j = requests.get("https://www.reddit.com/t/escape_from_tarkov/")
k = requests.get("https://www.reddit.com/t/nba/")
l = requests.get("https://www.reddit.com/t/megan_anderson/")
m = requests.get("https://www.reddit.com/t/atlanta_hawks/")
n = requests.get("https://www.reddit.com/t/los_angeles_lakers/")
o = requests.get("https://www.reddit.com/t/boston_celtics/")
p = requests.get("https://www.reddit.com/t/arsenal_fc/")
q = requests.get("https://www.reddit.com/t/philadelphia_76ers/")
r = requests.get("https://www.reddit.com/t/premier_league/")
s = requests.get("https://www.reddit.com/t/ufc/")
t = requests.get("https://www.reddit.com/t/arsenal_fc/")
u = requests.get("https://www.reddit.com/t/gamestop/")
v = requests.get("https://www.reddit.com/t/moderna/")
w = requests.get("https://www.reddit.com/t/pfizer/")
x = requests.get("https://www.reddit.com/t/johnson_johnson/")
y = requests.get("https://www.reddit.com/t/astrazeneca/")
z = requests.get("https://www.reddit.com/t/walgreens/")







a_s = BeautifulSoup(a.content, "html.parser")
b_s = BeautifulSoup(b.content, "html.parser")
c_s = BeautifulSoup(c.content, "html.parser")
d_s = BeautifulSoup(d.content, "html.parser")
e_s = BeautifulSoup(e.content, "html.parser")
f_s = BeautifulSoup(f.content, "html.parser")
g_s = BeautifulSoup(g.content, "html.parser")
h_s = BeautifulSoup(h.content, "html.parser")
i_s = BeautifulSoup(i.content, "html.parser")
j_s = BeautifulSoup(j.content, "html.parser")
k_s = BeautifulSoup(k.content, "html.parser")
l_s = BeautifulSoup(l.content, "html.parser")
m_s = BeautifulSoup(m.content, "html.parser")
n_s = BeautifulSoup(n.content, "html.parser")
o_s = BeautifulSoup(o.content, "html.parser")
p_s = BeautifulSoup(p.content, "html.parser")
q_s = BeautifulSoup(q.content, "html.parser")
r_s = BeautifulSoup(r.content, "html.parser")
s_s = BeautifulSoup(s.content, "html.parser")
t_s = BeautifulSoup(t.content, "html.parser")
u_s = BeautifulSoup(u.content, "html.parser")
v_s = BeautifulSoup(v.content, "html.parser")
w_s = BeautifulSoup(w.content, "html.parser")
x_s = BeautifulSoup(x.content, "html.parser")
y_s = BeautifulSoup(y.content, "html.parser")
z_s = BeautifulSoup(z.content, "html.parser")





print(a_s.get_text())
print(b_s.get_text())
print(c_s.get_text())
print(d_s.get_text())
print(e_s.get_text())
print(f_s.get_text())
print(g_s.get_text())
print(h_s.get_text())
print(i_s.get_text())
print(j_s.get_text())
print(k_s.get_text())
print(l_s.get_text())
print(m_s.get_text())
print(n_s.get_text())
print(o_s.get_text())
print(p_s.get_text())
print(q_s.get_text())
print(r_s.get_text())
print(s_s.get_text())
print(t_s.get_text())
print(u_s.get_text())
print(v_s.get_text())
print(w_s.get_text())
print(x_s.get_text())
print(y_s.get_text())
print(z_s.get_text())