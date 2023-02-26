import json
import time
from flask import Flask, request
from scraping import scrapheaal,request,filter_end,filter_start
from requests import get
import random
server = Flask(__name__)

@server.route("/")
def index():

 return "Lavander Api Hoşgeldiniz"
 

@server.route("/haberler")
def indexx():

 return scrapheaal()

@server.route("/enyuksek")
def indexxx():

 return request(filter_start(),filter_end())


@server.route("/depremler")
def depremler():
    r = get("https://api.orhanaydogdu.com.tr/deprem/live.php?limit=100") # orhanaydogdu special thx 
    return json.loads(r.content)


bilgi_list = ["Dolaplarınızı ve devrilebilecek benzeri eşyalar birbirine ve duvara sabitleyin.",
"Evde, iş yerinde, apartmanda, okulda afete hazırlık planları yapın.",
"Bir afet çantası hazırlamayı ve bu çantayı evin çıkışının yakınlarına koymayı unutmayın.",
"Önemli evraklarınızı (kimlik kartları, tapu, sigorta belgeleri) gibi kopyalarını hazırlayarak afet çantanızda bulundurun.",
"Gaz kaçağı ve yangına karşı, gaz vanası ve elektrik sigortaları otomatik hale getirin.",
"Depremden dolayı oluşabilecek yangına karşı yangın söndürme cihazı bulundurun ve periyodik bakımlarını yaptırın.",
"Depremden önce aile bireyleriniz ile iletişimin nasıl sağlanacağı ve alternatif buluşma yerleri hakkında ailenizle konuşun.",
"Tavan ve duvara asılan avize, klima vb. cihazlar bulundukları yere ağırlıklarını taşıyacak şekilde, duvar ve pencerelerden yeterince uzağa ve kanca ile asılmalıdır.",
"Deprem sırasında kesinlikle panik yapmayın.",
"Deprem sırasında sabitlenmemiş dolap, raf, pencere vb. eşyalardan uzak durun.",
"Deprem sırasında merdivenlere ya da çıkışlara doğru koşmayın.",
"Deprem sırasında balkonlardan ya da pencerelerden aşağıya atlanmayın.",
"Telefonlar acil durum ve yangınları bildirmek dışında kullanılmamalıdır.",
"Sarsıntı geçtikten sonra elektrik, gaz ve su vanalarını kapatılmalı, soba ve ısıtıcılar söndürülmelidir.",
"Güvenli bir yer bulup, diz üstü çökün, başınızı ve ensenizi, koruyacak şekilde kapanın, düşmemek için sabit bir yere tutunun.",
"Deprem anında dışarıda iseniz toprak altındaki kanalizasyon, elektrik ve gaz hatlarından gelecek tehlikelere karşı dikkatli olunmalıdır.",
"Deprem sırasında kibrit, çakmak yakılmamalı, elektrik düğmelerine dokunulmamalıdır.",
"Depremlerden sonra çıkan yangınlar oldukça sık görülen ikincil afetlerdir. Bu nedenle eğer gaz kokusu alırsanız, gaz vanasını kapatın.",
"Depremden sonra yerinden oynayan telefon ahizelerini telefonun üstüne koyun.",
"Depremden sonra cadde ve sokakları acil yardım araçları için boş bırakın.",
"Depremden sonra hasarlı binalardan ve enerji nakil hatlarından uzak durun.",
"Enkaz altındaysanız; el ve ayaklarınızı kullanabiliyorsanız su, kalorifer, gaz tesisatlarına, zemine vurmak suretiyle varlığınızı duyurmaya çalışın.", 
"Enkaz altındaysanız enerjinizi en tasarruflu şekilde kullanmak için hareketlerinizi kontrol altında tutun.",
"Sesinizi kullanabiliyorsanız kurtarma ekiplerinin seslerini duymaya ve onlara seslenmeye çalışın.",
"Depremden sonra artçı depremler tehlikesi sebebiyle binalara girmeyin.", 
"Metro ya da trende iseniz gerekmedikçe, kesinlikle metro ve trenden inilmemelidir. Elektriğe kapılabilirsiniz veya diğer hattan gelen başka bir metro yada tren size çarpabilir.", 
"Deprem anında ve sonrasında tsunami tehlikesi sebebi ile deniz kıyısından uzaklaşılmalıdır.", 
"Deprem anında pencerelerden ve camdan yapılmış eşyalardan uzak durulmalıdır.Deprem anında diğer güvenlik önlemleri alınarak gerekli olan eşya ve malzemeler alınarak bina daha önce tespit edilen yoldan derhal terk edilip toplanma bölgesine gidilmelidir.", 
"Deprem esnasında kesinlikle asansör kullanılmamalıdır."]



@server.route("/bilgi")
def bilgiler():
 veri = random.choice(bilgi_list)
 print(veri)
 json_data = {
 
  
  "bilgi" : veri,
  "author": "LavanderProjects",
  "status": "success"
}
 return (json_data)


if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
