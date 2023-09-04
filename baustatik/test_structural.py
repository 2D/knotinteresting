"""Provides a scripting component. 

    Inputs: 

        x: The x script variable 

        y: The y script variable 

    Output: 

        a: The a output variable""" 

  

__author__ = "d.demin" 

__version__ = "2023.02.16" 

  

import rhinoscriptsyntax as rs 

import math 

  

#solver 

  

#parameter 

#l = 6.5 #spannweite, m 

#t_a = 1200 #Trägerabstand, mm 

  

#Querschnitt 

###2 Balken  

#b2=200 #mm 

h2 = abs(h2) #mm 

A2 = b2*h2 

Iy2 = (b2 * math.pow(h2,3))/12 

  

print ("A2 = ",A2, "mm2") 

print (Iy2, "mm4") 

  

j = 3 #Anzahl Schichten 

#Schichtdichten 

j1 = 9 #mm 

j2 = 9 #mm 

j3 = 9 #mm 

s_d = ( j1 + j2 + j3 ) 

#Lagen in X 

jx = j/2 + 0.5 

#Lagen in Y 

jy = j/2 - 0.5 

h1 = j1 + j2 + j3 

  

""" 

Querschnittsparameter 

  

Balken Bestand C24 

  

""" 

  

E2 = 11000 #N/mm2 

roh2 = 3.70 #kN/mm2 

G2 = 690 #kN/mm2 

fmd2 = 14.1 #kN/mm2 

  

#Faktor Markquerschnitt 

mq = 1.0 #Faktor Markquerschnitt 

  

fvd1 = 1.5 

fvd2 = mq * 1.5 

  

print(fvd2,"N/mm2") 

  

#Mehrschichtplatte 

E1 = 11000 #N/mm2 

roh1 = 5.0 #kN/mm2 

G1 = 500 #kN/mm2 

fmd1 = 16.0 #kN/mm2 

fdv1 = 1.5 #N/mm2 

  

E1x = ((j1 + j3) / h1) * E1 

print( "E1x = %s N/mm2" % E1x ) 

  

#Mitwirkende Plattenbreite 

  

bf = (t_a - b2) 

print ("Mitwirkende Plattenbreite", bf/1000, "m") 

  

#Druckseite 

#befc = np.min( np.matrix( [ [bf/1000], [0.1* l], [20*h1/1000] ] ) ) 

befc = min( bf/1000, 0.1* l, 20*h1/1000 ) 

print ("befc =", befc) 

  

b1 = b2/1000 + befc 

print ("b1 = %s m" % (b1) ) 

A1 = b1 * h1 

print ("A1 = %s mm2" % A1) 

Iy1 = (b1 * math.pow(h1,3))/12 

print (Iy1, "mm4") 

  

#Kombinierter Querschnitt 

#Verbindungsmittel 

#starre Pressverklebung vor Ort 

y1 = 0.5 

y2 = 1.0 

  

hgesamt = h1 + h2 

A2_m = A2 / 1000000 

A1_m = A1/1000 

a_2 = ( y1 * E1x * A1 * hgesamt) / ( 2 * ( (y1 * E1x * A1_m) + (y2 * E2 * A2_m) ) ) 

a_2 =a_2/1000 

print ("a2 = %s mm" % a_2) 

  

a_1 = hgesamt - (h1/2) - (h2/2) - a_2 

  

print ( "a1 = %s mm" % a_1 ) 

  

EIeff =  ( E1x *math.pow(10,6) ) * ( Iy1*math.pow(10,-9) ) + y1 * (E1x *math.pow(10,6)) * A1_m * (math.pow(a_1,2)*math.pow(10,-6))  

EIeff += ( E2 * math.pow(10,6) ) * ( Iy2*math.pow(10,-12) ) + y2 * (E2 * math.pow(10,6)) * A2_m * (math.pow(a_2,2)*math.pow(10,-6)) 

print ("EIeff = %s Nmm2" % EIeff ) 

  

AGes = A1_m + A2_m 

AGes_mm = AGes*1000000 

print "AGes_mm %s mm2" % AGes_mm 

  

#Auflast 

  

gAk = 3 * t_a /1000 

  

print ( "Auflast gAk = %s kN/m" %gAk ) 

  

#Nutzlast Versammlung 

qk = 3 * t_a /1000 

  

print ( "Nutzlast Versammlung qk = %s kN/m" %qk ) 

  

#Eigenlast Holzdecke 

  

VLamellen = h1 * t_a /1000000 

  

gkLamellen = VLamellen * roh1 

  

gkSteg = A2_m * roh2 

  

gk = gkLamellen + gkSteg 

  

#Tragsicherheit 

  

qd = 1.35 * (gAk + gk) + 1.5 * qk 

print ( "Tragsicherheit (qd) = %s kN/m" % qd) 

  

#Biegemoment 

Med = (qd * math.pow(l,2))/8 

print ( "Biegemoment (Med) = %s kN/m" % Med) 

  

#Bemessungswert der Randspannung 

om1d = ( Med/EIeff ) * E1x * ( y1*a_1 + h1/2 ) 

print "Nachweis Randspannung om1d/fmd1 ", ("%s is <1.0" %(om1d/fmd1) if om1d/fmd1 <= 1.0 else "not OK") 

  

om2d = Med/EIeff*E2*(y2*a_2+h2/2) 

print "Nachweis Randspannung om2d/fmd2 ", ("%s is <1.0" %(om2d/fmd2) if om2d/fmd2 <= 1.0 else "not OK") 

  

#Bemessungswert der Druckspannung im Schwerpunkt des Querschnittes 1 & 2: 

ofc1d = Med/EIeff * E1x * y1 * a_1 

print "ofc1d = %s N/mm2" % ofc1d, "; Nachweis Druckspannung im Schwerpunkt ofc1d/fmd1 ", ("%s is < 1.0" %(ofc1d/fmd1) if ofc1d/fmd1 <= 1.0 else "not OK") 

ofc2d = Med/EIeff * E2 * y2 * a_2 

print "ofc2d = %s N/mm2" % ofc2d, "; Nachweis Druckspannung im Schwerpunkt ofc12d/fmd2 ", ("%s is < 1.0" %(ofc2d/fmd2) if ofc2d/fmd2 <= 1.0 else "not OK") 

  

#Querkraft 

Ved = qd*l/2 

print ( "Querkraft = %s kN" % Ved ) 

#Bemessungswert der Schubspannung in der y-Achse 

t_max2d = ( Ved / (b2*EIeff) ) * ( (E2*b2* (math.pow(h2,2)/2) ) ) 

t_max2d = t_max2d/1000 

print "t_max2d = %s N/mm2" % t_max2d, "; Nachweis Schubspannung t_max2d/fvd2 ", ("%s is < 1.0" %(t_max2d/fvd2) if t_max2d/fvd2 <= 1.0 else "t_max2d/fvd2 at value %s is not OK" %(t_max2d/fvd2) )  

  

#Bemessungswert der Schubspannung in der Fuge 

t_Fuge1d = Ved/ (b2*EIeff) * y1 * E1x * A1 * a_1 

print "t_Fuge1d = %s N/mm2" % t_Fuge1d, "; Nachweis Fugenschubspannung t_Fuge1d/fvd1 ", ("%s is < 1.0" %(t_Fuge1d/fvd1) if t_Fuge1d/fvd1 <= 1.0 else "t_max2d/fvd2 at value %s is not OK" %(t_Fuge1d/fvd1) )  

  

#Querkraftwiderstand nur Träger: 

VRdT = (fvd2*b2*h2) / 1000 

t_d = ( 1.5 * Ved/(b2*h2) ) * 1000 

print "VRdT = %s kN; " % VRdT, "t_d = %s N; " % t_d 

  

#Querkraftwiderstand nur Platte 

VRdL = fvd1*b1*h1 

print "Querkraftwiderstand nur Platte = %s kN; " % VRdL 

  

#Gebrauchstauglichkeit im Grenzzustand Aussehen 

#Kurzzeit 

qdGK = gAk + gk + 0.7 * qk 

wzul = l/350 * 1000 

print qdGK, ";", wzul 

  

wed0 = ( ( (5*qdGK* math.pow(l,4)) / (384*EIeff) ) + ( (qdGK* math.pow(l,2) ) / (8*G2*A2) ) ) * 1000000 

print "wed0 = %s mm" % wed0, "; Nachweis wed0/wzul ", ("%s is < 1.0" %( wed0/wzul ) if wed0/wzul <= 1.0 else "wed0/wzul at value %s is not OK" %(wed0/wzul) )  

  

#Durchbiegungen Langzeit in Feldmitte Langzeit phi=1 

qdGL = gAk+gk 

  

phi = 1.0 

wed = ( ((5*qdGL* math.pow(l,4) ) / (384*EIeff) )    +      ( (qdGL*math.pow(l,2))/(8*G2*A2) ) )  *   ( 1+ (phi*(1/1)) ) 

wed = wed * math.pow(10,6) 

print "wed = %s mm" % wed, "; Nachweis wed/wzul ", ("%s is < 1.0" %( wed/wzul ) if wed/wzul <= 1.0 else "wed0/wzul at value %s is not OK" %(wed/wzul) )  

print math.pow(10,2), 10.0**2 

  

test = wed/wzul 