from Crypto.Util.number import *
import os
from secret import FLAG

z1 = getStrongPrime(512)
z2 = getStrongPrime(512)
n = z1*z2
e = 65537
c = pow(bytes_to_long(FLAG), e, n)
print(f'{e = }')
print(f'{c = }')
print(f'{n = }')

z3 = getPrime(256)
modd = getPrime(2048)
rand_1 = bytes_to_long(os.urandom(128))
rand_2 = bytes_to_long(os.urandom(128))

hidden_val = z2*z3*z1 + rand_1
hint_1 = (z3**8)*z2 + 0x1337*z2*(z1**2) + rand_2
hint_2 = pow(hidden_val, 4*modd, modd)
print(f'{modd = }')
print(f'{hint_1 = }')
print(f'{hint_2 = }')

'''
e = 65537
c = 84024814852788124466425703643863038749481647370871639089654387542036643094716882068963882238496325769187878841775880081279152499243027962801549637300718551708561273294208652726640622690307777302333680477067048191391930158103357680194404771799199270457029205340289309827037753672155563351056992825762854051224
n = 158463604064988674814039489303941776312791739197627574932768489648690514396703416035754401039816044989153946047961788657502924899489831181881976797925405205879265356891684604165414639744668756045525079746390221907286699345190568138908374561952476963068186895955907054769899744946840855438948702842692818992193
modd = 28380446321095327045197943237561249132818639849632383597957781139459442976484022092235551323350873442219988496936317243060695903464196236518499415107693912425146869970931590379094106285244897949112170793149963425649014239104215833842814257009714057533568025678694679554857780851646426228532250750372305903959916291671627585809053461591194382116337570074638325015114805604072385544025035377829638386785120688334551740081467841719585730908022128079866130687361608669542661116817147325164173681733966300168129858129906169569291487066119040715366582183828675478522478096526885343420675985370458086475314154595337857476899
hint_1 = 81813119979744357303763165097277937958832393933373338098275076650301553027527996054129758821806150335067485819738432997780039994547616390541448175462514726116257489583525965719006176585106201077096492640208154851064083081914900991051522865322141804472360190857895241232523630699727605379452784521665518271731063633536742217058852820964499079832842067879422070222355944056878164298442422556194511015260428242217865176134094577687217869008146710683271174759372846052837009048977507229936211604102332267749999555281976244071174858943184520818940571841826590657426078269047245626706453929118608324689256506522595415935025982865082986683254070145179665083950019654924243468765457223868455752542625019204956397050465933928837910298798965289994071762528071761825840693055585978
hint_2 = 27872414423465448839008773252984934772605719582797604107400025164483385719784673459001870474899649741532172662873918849102732485354302202273013886322871653304670348649815599453000867456436627341218257642397825784866634073432088498094539521178347661960267331856611511482626787017628514069684088467972502594418477709846241043641201390263493109943593831233932533247678368852492825347202862149127452288558425333271311280901410346177052060600869643714013453208193185985858182886761151009370197259832926917172521983662323385684859034242173578700705333395684973560554585616346907697449205320331840873031302298561500826369956
'''