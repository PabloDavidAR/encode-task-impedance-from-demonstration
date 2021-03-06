#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray, Bool
from threading import Thread
from threading import Lock
from inputs import get_gamepad

end = False
obj = Lock()
name_node = "gamePad"

example = [
        [
            -0.20197117359697805,
            -0.1850416724794888,
            0.4005012277050681
        ],
        [
            -0.20197129610108513,
            -0.18502536624625918,
            0.4004549086147227
        ],
        [
            -0.20193421552793037,
            -0.18499801271589558,
            0.40033658606767664
        ],
        [
            -0.20190726131593265,
            -0.18498497967086006,
            0.40024413336312803
        ],
        [
            -0.2018835537792887,
            -0.18496068921602096,
            0.40009662730636936
        ],
        [
            -0.20187338284369558,
            -0.184955789367053,
            0.39995217440517117
        ],
        [
            -0.2018700625988627,
            -0.1849640760095758,
            0.3998402545344749
        ],
        [
            -0.20186175037247017,
            -0.18495665339560555,
            0.39966827757191126
        ],
        [
            -0.20185757818831224,
            -0.18495674857548655,
            0.3995019106793264
        ],
        [
            -0.2018116547554758,
            -0.18494609311384272,
            0.399367613747671
        ],
        [
            -0.20178681468194565,
            -0.18493172024475701,
            0.39918559148051364
        ],
        [
            -0.2017357310079688,
            -0.18493339968964384,
            0.3989950247823829
        ],
        [
            -0.2016974835265425,
            -0.18491025546844964,
            0.39880700357472315
        ],
        [
            -0.20165382423929562,
            -0.18491060508983456,
            0.39859509941536386
        ],
        [
            -0.20161172510741385,
            -0.18489710409979754,
            0.39840026042476584
        ],
        [
            -0.20155612465163167,
            -0.18489346787300492,
            0.3981853838457134
        ],
        [
            -0.20151147954343018,
            -0.18487785772426715,
            0.3979711606720944
        ],
        [
            -0.20145556122239786,
            -0.18487016956155553,
            0.39769412963957257
        ],
        [
            -0.20140258263861843,
            -0.18485453891061687,
            0.39747490123976864
        ],
        [
            -0.20135543196147299,
            -0.1848302629891188,
            0.3971881881735445
        ],
        [
            -0.2012822515756687,
            -0.18483687639250224,
            0.39691897516962993
        ],
        [
            -0.20122544791249772,
            -0.1848110588933248,
            0.39662488180001587
        ],
        [
            -0.20114532561797824,
            -0.18479908330127612,
            0.39625554542665475
        ],
        [
            -0.20107102002542027,
            -0.1847761097673695,
            0.39592981802971905
        ],
        [
            -0.20098403896268424,
            -0.18476112407013323,
            0.39552527597378495
        ],
        [
            -0.2008870991904532,
            -0.1847457070658308,
            0.39515656602963584
        ],
        [
            -0.20080955469668538,
            -0.1847270209571042,
            0.3947870561131461
        ],
        [
            -0.20071750843383343,
            -0.1847093437823144,
            0.394406515697095
        ],
        [
            -0.20062460960086134,
            -0.18469175350809489,
            0.3939557121306884
        ],
        [
            -0.2005198729826736,
            -0.18465907507069657,
            0.39349313219372767
        ],
        [
            -0.20041108848771602,
            -0.1846371954280683,
            0.3929792745740185
        ],
        [
            -0.20027911313015462,
            -0.1846146680057717,
            0.3925033670381487
        ],
        [
            -0.20017207531352524,
            -0.18459461705830565,
            0.39199464964604114
        ],
        [
            -0.20004824194382356,
            -0.18456302271763395,
            0.3914744361307594
        ],
        [
            -0.19992961528251096,
            -0.18453073482767934,
            0.3909008565442622
        ],
        [
            -0.19977877706694247,
            -0.18451487171864026,
            0.39028557101768335
        ],
        [
            -0.1996144843278128,
            -0.18448637073517832,
            0.3896588603887496
        ],
        [
            -0.1994867776887655,
            -0.1844566490882625,
            0.3890086220911104
        ],
        [
            -0.19933798943909226,
            -0.1843997395598072,
            0.3883153622174365
        ],
        [
            -0.1991279601220202,
            -0.18436900894087282,
            0.3875264730024516
        ],
        [
            -0.19894117714616488,
            -0.18432525582134326,
            0.38677377288076575
        ],
        [
            -0.19874310037924695,
            -0.1842982164555914,
            0.3860022588813594
        ],
        [
            -0.19855750834774658,
            -0.18425884734837963,
            0.3852393424464997
        ],
        [
            -0.19837841869838346,
            -0.18420253964373628,
            0.38440881889615464
        ],
        [
            -0.19816286015757673,
            -0.18416159802700072,
            0.3836384937743133
        ],
        [
            -0.19798577288461888,
            -0.18411936963373013,
            0.3828583358455343
        ],
        [
            -0.19780375900949537,
            -0.1840830173443338,
            0.3821352454660606
        ],
        [
            -0.19762460553923153,
            -0.18404526931261025,
            0.3814228430262
        ],
        [
            -0.1974488020725708,
            -0.18399360889756072,
            0.38073815836438635
        ],
        [
            -0.1972953312062415,
            -0.18396908617327978,
            0.3801317033618448
        ],
        [
            -0.19716196939609176,
            -0.1839454896380053,
            0.3795929010017992
        ],
        [
            -0.19705964094718414,
            -0.18391800229403824,
            0.37922151576257046
        ],
        [
            -0.1969182310440588,
            -0.18389307656959206,
            0.3787196892468985
        ],
        [
            -0.19683997328646485,
            -0.18387795260016082,
            0.3783964032658385
        ],
        [
            -0.1967864117703818,
            -0.18387377904384006,
            0.3781869326245917
        ],
        [
            -0.1967737880422678,
            -0.1838550410487506,
            0.37805857079985195
        ],
        [
            -0.1967591300613754,
            -0.18387037278430818,
            0.3781223029278307
        ],
        [
            -0.19679070379959648,
            -0.18386539350047593,
            0.37819816012809204
        ],
        [
            -0.1968632889429126,
            -0.18388896981534517,
            0.3784243089656504
        ],
        [
            -0.1969276373789986,
            -0.18389869220090313,
            0.3786330234576867
        ],
        [
            -0.19699798414425085,
            -0.183897475249161,
            0.3788562841554566
        ],
        [
            -0.19706952471231629,
            -0.1839101198559588,
            0.37910723546433106
        ],
        [
            -0.19712449512092378,
            -0.1839265510062705,
            0.3792886568941166
        ],
        [
            -0.19717593962079824,
            -0.18393042499933177,
            0.37949505371202447
        ],
        [
            -0.19722136623449926,
            -0.1839399072572962,
            0.37969561806717783
        ],
        [
            -0.19724152058827155,
            -0.18394627834606736,
            0.3798107832559363
        ],
        [
            -0.19728996781242325,
            -0.18395962638213856,
            0.379940660964766
        ],
        [
            -0.19732604942334897,
            -0.18396047154711034,
            0.3800612884502522
        ],
        [
            -0.1973352469287204,
            -0.18396691667917345,
            0.3801144911616108
        ],
        [
            -0.19735449984998185,
            -0.1839616933696397,
            0.38018474794257384
        ],
        [
            -0.19737463473337072,
            -0.18397198396325312,
            0.3802821370742273
        ],
        [
            -0.1973815004410062,
            -0.18399039934981226,
            0.380328377164998
        ],
        [
            -0.19741616796686604,
            -0.18399256965471486,
            0.3804517918425374
        ],
        [
            -0.19746207400466098,
            -0.1839873470816736,
            0.3805755143558424
        ],
        [
            -0.19747504050115525,
            -0.18400604443725302,
            0.38074217571302305
        ],
        [
            -0.19753045345344122,
            -0.18400721370647255,
            0.3809276960955689
        ],
        [
            -0.1975990466736527,
            -0.18401535648988457,
            0.3811148931987066
        ],
        [
            -0.19767399775338834,
            -0.184031821680273,
            0.3813768040790776
        ],
        [
            -0.19771518422269213,
            -0.18404994906699224,
            0.3816352753748724
        ],
        [
            -0.1977849912466833,
            -0.1840591332124344,
            0.38189514572600575
        ],
        [
            -0.19787287734111114,
            -0.18407216823965505,
            0.38223090076236665
        ],
        [
            -0.19795307040943888,
            -0.18408957784305913,
            0.38249163154781407
        ],
        [
            -0.19804679069128966,
            -0.18412528876737383,
            0.3828964420099958
        ],
        [
            -0.19815043033674878,
            -0.1841246416469495,
            0.3833289280541057
        ],
        [
            -0.19827128608006017,
            -0.18415070483478083,
            0.38379593238322646
        ],
        [
            -0.19841518536990824,
            -0.18418015027470744,
            0.3842942745578857
        ],
        [
            -0.1985204823757972,
            -0.184204257786146,
            0.38478948423830217
        ],
        [
            -0.19868233548662323,
            -0.18423456297766747,
            0.3854385758299337
        ],
        [
            -0.1988606765601096,
            -0.18428597856442352,
            0.38621381618231376
        ],
        [
            -0.19903602830389155,
            -0.1843101787058458,
            0.3869033660955706
        ],
        [
            -0.19920168880761435,
            -0.1843638952018509,
            0.3876196538527221
        ],
        [
            -0.19937412160294207,
            -0.18438232062346982,
            0.3883217749634204
        ],
        [
            -0.1995757551684422,
            -0.18441737005562073,
            0.3890430858811393
        ],
        [
            -0.1997034700823625,
            -0.18447920029213552,
            0.38973624635396487
        ],
        [
            -0.1998725492349517,
            -0.1844930406077419,
            0.39042885010248884
        ],
        [
            -0.20001847352506524,
            -0.18453433422762733,
            0.3910999064527472
        ],
        [
            -0.2001938158703505,
            -0.18456474838660486,
            0.3918113296654241
        ],
        [
            -0.20034727075755757,
            -0.18459586050520957,
            0.39245457166225123
        ],
        [
            -0.20049848222416614,
            -0.18463118663625966,
            0.3930993524095906
        ],
        [
            -0.2006445429841102,
            -0.18466778256839214,
            0.39375244978365853
        ],
        [
            -0.20079072018350708,
            -0.18469969413648016,
            0.3943833768581683
        ],
        [
            -0.20093666899970272,
            -0.18472197224464895,
            0.394980457820817
        ],
        [
            -0.20105250063000657,
            -0.18475724493371995,
            0.3955401856341601
        ],
        [
            -0.20116429216532228,
            -0.18477817062261356,
            0.39608412299901946
        ],
        [
            -0.20128353992803297,
            -0.1847927034977484,
            0.3965138363184386
        ],
        [
            -0.20141605682307948,
            -0.1848263189332765,
            0.39711497353749015
        ],
        [
            -0.2015066835492924,
            -0.1848520274438374,
            0.397611092140678
        ],
        [
            -0.20159594939434966,
            -0.1848643804549307,
            0.3980271522182037
        ],
        [
            -0.20169278534803164,
            -0.18487638410464158,
            0.3983894955891469
        ],
        [
            -0.20177538766954933,
            -0.18489148185961488,
            0.3987207877143736
        ],
        [
            -0.20184602194539167,
            -0.18491260294327022,
            0.3990344082479902
        ],
        [
            -0.20188833193663333,
            -0.18492045314568872,
            0.3992611484794724
        ],
        [
            -0.201921020379059,
            -0.18493103196004698,
            0.3994642084825517
        ],
        [
            -0.20196641776251364,
            -0.18492918286016022,
            0.39963463549858025
        ],
        [
            -0.2019812315755825,
            -0.18494698392534195,
            0.3997133627064977
        ],
        [
            -0.2019891866520926,
            -0.18493581378368149,
            0.39974022105598495
        ],
        [
            -0.20197823414366162,
            -0.18494287761308909,
            0.3997261214693957
        ],
        [
            -0.20197578502419664,
            -0.18494530522463787,
            0.39970714788404477
        ],
        [
            -0.20195500263530616,
            -0.1849496058561192,
            0.39972953712633513
        ],
        [
            -0.20196698923144693,
            -0.1849446373138671,
            0.39970134368791566
        ],
        [
            -0.20198316769409488,
            -0.1849406188141794,
            0.39971173519354464
        ],
        [
            -0.20197947224607612,
            -0.18494973445767424,
            0.3997311909751795
        ],
        [
            -0.20199005613166807,
            -0.1849332552004535,
            0.39970529177731484
        ],
        [
            -0.20197016136500662,
            -0.18494817908447284,
            0.3997125075233158
        ],
        [
            -0.20196304302377444,
            -0.18493891121189682,
            0.3997021380470637
        ],
        [
            -0.20196733850934873,
            -0.184942462697155,
            0.3997303844440735
        ],
        [
            -0.20197309350854226,
            -0.1849401018344681,
            0.3997296347933434
        ],
        [
            -0.20197290404561014,
            -0.18494991342046854,
            0.39972335550100674
        ],
        [
            -0.2019738810392678,
            -0.1849483657917552,
            0.3996949981318639
        ],
        [
            -0.20195723940905114,
            -0.1849444451726974,
            0.39972742638134484
        ],
        [
            -0.20196642809587745,
            -0.18495445636635574,
            0.39972392770053067
        ],
        [
            -0.20198312114486666,
            -0.18494668962470062,
            0.3997223607614281
        ],
        [
            -0.20197994040747114,
            -0.18494868108677942,
            0.3997078819087002
        ],
        [
            -0.20197069015195437,
            -0.18494281515646918,
            0.3997019030069696
        ],
        [
            -0.20196330435197019,
            -0.18494992701345608,
            0.3997466692540677
        ],
        [
            -0.20197198684640083,
            -0.18494439495230958,
            0.39971889335526145
        ],
        [
            -0.20197078726685744,
            -0.18494414504904774,
            0.39972834557380466
        ],
        [
            -0.20197537158070888,
            -0.18495049937928645,
            0.3997008510790276
        ],
        [
            -0.20196886699371527,
            -0.18494400864697338,
            0.39970411621316504
        ],
        [
            -0.2019644223228896,
            -0.18494321970515973,
            0.3996944702152929
        ],
        [
            -0.20197003838564437,
            -0.18494074801483104,
            0.39970864534169886
        ],
        [
            -0.20197355881960968,
            -0.18493805222357967,
            0.3997282127151802
        ],
        [
            -0.20196584235088993,
            -0.18494146733446443,
            0.39971285162226355
        ],
        [
            -0.20196985976991613,
            -0.18494643422436893,
            0.3997059529021812
        ],
        [
            -0.2019658929666451,
            -0.18494823387063306,
            0.39971104084576814
        ],
        [
            -0.20197514391280355,
            -0.18494329201609058,
            0.3997255326619912
        ],
        [
            -0.20197598755876842,
            -0.1849444009707439,
            0.3997029886072969
        ],
        [
            -0.20196613047797818,
            -0.18495302085881624,
            0.3996924206416272
        ],
        [
            -0.2019724343422818,
            -0.1849472417492687,
            0.3996936134468164
        ],
        [
            -0.20196768284545955,
            -0.18494216776721661,
            0.39968579932707116
        ],
        [
            -0.2019700786595728,
            -0.1849396642971959,
            0.399725567446672
        ],
        [
            -0.20197384193327236,
            -0.18493965962756925,
            0.39973001321231305
        ],
        [
            -0.20197390295950798,
            -0.18494053160754523,
            0.39970107917190767
        ],
        [
            -0.20196248670029976,
            -0.18495201203806141,
            0.399687491081565
        ],
        [
            -0.20197044162743286,
            -0.18495250521340112,
            0.39972089487466106
        ],
        [
            -0.2019614492875891,
            -0.18494184055677312,
            0.39968944754738545
        ],
        [
            -0.2019845270916854,
            -0.18493955184705566,
            0.3997076930456246
        ],
        [
            -0.2019880821615609,
            -0.18493699340893346,
            0.39971517184941885
        ],
        [
            -0.20197644337028997,
            -0.18494751529584358,
            0.39969263161237767
        ],
        [
            -0.20196656422190398,
            -0.18493847280805417,
            0.39969117629098444
        ],
        [
            -0.2019850676195471,
            -0.184941852648228,
            0.39970347574756065
        ],
        [
            -0.2019693434799565,
            -0.184941633987124,
            0.39968627406408225
        ],
        [
            -0.2019741177124051,
            -0.18494497914205527,
            0.39969774315130385
        ],
        [
            -0.20195517361130103,
            -0.18495475245961468,
            0.3996996609509129
        ],
        [
            -0.20196144802717467,
            -0.18495015176019308,
            0.39968928015005434
        ],
        [
            -0.20197040587266388,
            -0.18494161841303727,
            0.39968173363649406
        ],
        [
            -0.20196893157137957,
            -0.18495264646088455,
            0.39968339820980614
        ],
        [
            -0.2019855775284462,
            -0.18494169851169653,
            0.39970381554122125
        ],
        [
            -0.20196508994751414,
            -0.18494236763876912,
            0.39969796068101615
        ],
        [
            -0.20195824434686122,
            -0.18494728993430679,
            0.3996828966395144
        ],
        [
            -0.20196186440216496,
            -0.18494682884970293,
            0.399687602557598
        ],
        [
            -0.20196234751718747,
            -0.18495017421538723,
            0.3997207791841205
        ],
        [
            -0.2019876479977032,
            -0.18493711851369704,
            0.3997230397011284
        ],
        [
            -0.20197113372323927,
            -0.18494464380155823,
            0.3997055080488195
        ],
        [
            -0.20198064949314803,
            -0.18495010190549666,
            0.3996832934601736
        ],
        [
            -0.20196702290881458,
            -0.18494155178193838,
            0.39969175350563796
        ],
        [
            -0.20196781391597368,
            -0.1849421667281224,
            0.3996929684446984
        ],
        [
            -0.20197362322522736,
            -0.18493617854822283,
            0.3996942943057307
        ],
        [
            -0.20194620126902946,
            -0.18494844900248847,
            0.399699341404688
        ],
        [
            -0.20198439769074067,
            -0.18494102768477422,
            0.3997270039188402
        ],
        [
            -0.20197347844453062,
            -0.18494219395906114,
            0.3997032139151109
        ],
        [
            -0.2019759025454959,
            -0.18494541530101213,
            0.3996936904008661
        ],
        [
            -0.20195912936047983,
            -0.18494771929146284,
            0.3997033597510524
        ],
        [
            -0.20196813061894128,
            -0.18493140968733943,
            0.3996798042597152
        ],
        [
            -0.20196754128048622,
            -0.1849436928457618,
            0.3997112025414755
        ],
        [
            -0.20197060961295785,
            -0.18494753749116102,
            0.3996984608687175
        ],
        [
            -0.2019682496265129,
            -0.18494356433356685,
            0.3997086948010964
        ],
        [
            -0.2019698512857192,
            -0.1849388345455187,
            0.39967987673474675
        ],
        [
            -0.20196179680637988,
            -0.18494743179599432,
            0.3997060174577435
        ],
        [
            -0.2019858285507805,
            -0.184946977957701,
            0.3996989796974725
        ],
        [
            -0.20197969713759947,
            -0.18493708788780983,
            0.3997209936807721
        ],
        [
            -0.20197226655128267,
            -0.18493924991343091,
            0.3997038350123088
        ],
        [
            -0.20197878393312707,
            -0.18494837176705395,
            0.3997063248430632
        ],
        [
            -0.20197069995994943,
            -0.1849477839823212,
            0.39968473185557707
        ],
        [
            -0.20197464380048813,
            -0.18493496924239738,
            0.39970661916488986
        ],
        [
            -0.2019651785483796,
            -0.18494452190142796,
            0.39969875015588124
        ],
        [
            -0.2019583004051908,
            -0.18494207687867187,
            0.39970355648614847
        ],
        [
            -0.20197430580635653,
            -0.18494277529068975,
            0.3996734841784763
        ],
        [
            -0.20195501999047274,
            -0.18494591359550652,
            0.39967790135970105
        ],
        [
            -0.2019639262299514,
            -0.1849531105539574,
            0.39969585672352304
        ],
        [
            -0.20196329643979877,
            -0.18493471830244546,
            0.39971035585227566
        ],
        [
            -0.2019763801294407,
            -0.1849415835064834,
            0.39971972486970114
        ],
        [
            -0.20196115221315922,
            -0.18494644577923092,
            0.3996931278980622
        ],
        [
            -0.20196782641343838,
            -0.18495162331455708,
            0.3996774630665346
        ],
        [
            -0.20195987724701625,
            -0.18494152038428407,
            0.3997262906341899
        ],
        [
            -0.20197062557449294,
            -0.1849409551003973,
            0.3997095913499807
        ],
        [
            -0.201959418453083,
            -0.18494800732332703,
            0.3996774293032599
        ],
        [
            -0.20198079615383144,
            -0.18493404474287234,
            0.3996884195753333
        ],
        [
            -0.2019742746845377,
            -0.18492241575942922,
            0.3996883885068354
        ],
        [
            -0.20196973372408347,
            -0.18494924600993812,
            0.3997046381197147
        ],
        [
            -0.20197365077221774,
            -0.18494029702574363,
            0.39967124634329587
        ],
        [
            -0.20196085957448665,
            -0.18494324279610855,
            0.399691536729866
        ],
        [
            -0.20196947453857084,
            -0.18494338638118443,
            0.39968301432343245
        ],
        [
            -0.20196945367728494,
            -0.18494656365275092,
            0.39970390435646685
        ],
        [
            -0.20196101157427554,
            -0.18495115714114285,
            0.3997011515989528
        ],
        [
            -0.20198198831924957,
            -0.1849342412607872,
            0.39968140870105057
        ],
        [
            -0.20197302781690013,
            -0.18494051482072285,
            0.3996876582532137
        ],
        [
            -0.201976990792462,
            -0.18494094597098726,
            0.39969875534185184
        ],
        [
            -0.2019728489051918,
            -0.18494411543096015,
            0.3996662217053186
        ],
        [
            -0.20196799748827207,
            -0.1849429629160626,
            0.3996926793022403
        ],
        [
            -0.20196759286919574,
            -0.18495556470374977,
            0.39966999484659016
        ],
        [
            -0.2019776153633007,
            -0.18493920268981462,
            0.39968051341392946
        ],
        [
            -0.20195259424752748,
            -0.1849440109296113,
            0.3996744692896619
        ],
        [
            -0.2019774933789617,
            -0.18494370182323147,
            0.3996918368872942
        ],
        [
            -0.20196284743258802,
            -0.1849443096845632,
            0.39968360746943254
        ],
        [
            -0.20197417561612027,
            -0.18493830600993372,
            0.39971113629218746
        ],
        [
            -0.20197144608138828,
            -0.18494000229327648,
            0.39970443545477063
        ],
        [
            -0.20197846272706801,
            -0.18494738137414357,
            0.39968453498849843
        ],
        [
            -0.20197189748107694,
            -0.1849397879871455,
            0.3996818407860472
        ],
        [
            -0.20196581193261895,
            -0.18492801286723165,
            0.39969131660627777
        ],
        [
            -0.2019697562625603,
            -0.18494307409180968,
            0.39969503341986967
        ],
        [
            -0.2019574352875128,
            -0.18494574007048936,
            0.3996800947538997
        ],
        [
            -0.2019557161185761,
            -0.18494861373384755,
            0.39970236062352266
        ],
        [
            -0.2019588959778266,
            -0.18494056498636272,
            0.3996958330553365
        ],
        [
            -0.20195947475990886,
            -0.18493673520829887,
            0.39968246008349734
        ],
        [
            -0.20196029577450883,
            -0.18494663699311464,
            0.39968727482981214
        ],
        [
            -0.20197306964747297,
            -0.18493632135647847,
            0.3996690918056438
        ],
        [
            -0.2019570759541404,
            -0.18495663490616673,
            0.39968902840157805
        ],
        [
            -0.2019594112851051,
            -0.18494599194249015,
            0.3996716657544342
        ],
        [
            -0.20196115680112317,
            -0.1849358442631952,
            0.3996881296369268
        ],
        [
            -0.20198300043876632,
            -0.18494565705924262,
            0.3997022037960565
        ],
        [
            -0.20195420580671614,
            -0.18494356699623793,
            0.39969031683300693
        ],
        [
            -0.20197895439769026,
            -0.18493831168469063,
            0.39967947403715165
        ],
        [
            -0.20196598774969027,
            -0.18494232301780758,
            0.39967986546976364
        ],
        [
            -0.2019641254851819,
            -0.1849413253329175,
            0.3996770299300872
        ],
        [
            -0.2019559453842346,
            -0.18494979203035544,
            0.3996986355060569
        ],
        [
            -0.20197440900845248,
            -0.1849371670615217,
            0.3996674697023884
        ],
        [
            -0.20197731299121427,
            -0.18493753893558676,
            0.39968951469234115
        ],
        [
            -0.20197216142707025,
            -0.18494302303490126,
            0.39966015189677023
        ],
        [
            -0.20196212177021908,
            -0.18494222343676203,
            0.3996888970608411
        ],
        [
            -0.20196348581086934,
            -0.18494513361992398,
            0.399690268292608
        ],
        [
            -0.20196324096196366,
            -0.18494076123803227,
            0.399686192590292
        ],
        [
            -0.20196747841602877,
            -0.18493880122808695,
            0.39969564733793217
        ],
        [
            -0.20195929885144143,
            -0.1849478505832532,
            0.399671879950001
        ],
        [
            -0.2019622262958344,
            -0.1849441634242146,
            0.3996818511281593
        ],
        [
            -0.20196646618378544,
            -0.18493760599950673,
            0.39967987809108957
        ],
        [
            -0.20196028982255054,
            -0.18495107806305908,
            0.39967410441535384
        ],
        [
            -0.201964049317296,
            -0.18494497829505926,
            0.39968269550373914
        ],
        [
            -0.2019504068452151,
            -0.18495044661237567,
            0.3996786889052748
        ],
        [
            -0.201958720188554,
            -0.1849448431317954,
            0.39968288037348015
        ],
        [
            -0.20196890259183367,
            -0.18494514446231028,
            0.3996657439252752
        ],
        [
            -0.20194664321273856,
            -0.1849456891589105,
            0.3996816773146968
        ],
        [
            -0.20195862814325674,
            -0.18494819821985584,
            0.39967508791891526
        ],
        [
            -0.20194108679419015,
            -0.18495257840063817,
            0.399650995985785
        ],
        [
            -0.20196923471634987,
            -0.18494237379943818,
            0.3996579942426164
        ],
        [
            -0.2019530832988064,
            -0.18494243493928714,
            0.39966552997254207
        ],
        [
            -0.2019486832059458,
            -0.18494700296481062,
            0.3996688957305017
        ],
        [
            -0.20196178631594727,
            -0.18494491664063398,
            0.3996826720119898
        ],
        [
            -0.20195816714309608,
            -0.18495055904905705,
            0.39967615342969504
        ],
        [
            -0.2019611344497942,
            -0.18495117229841773,
            0.39968912872264845
        ],
        [
            -0.2019710508043494,
            -0.18493972691208235,
            0.39967697012619063
        ],
        [
            -0.2019571511053944,
            -0.1849500478019502,
            0.3996722287676898
        ],
        [
            -0.20195044285002545,
            -0.1849447167975711,
            0.3996339398202679
        ],
        [
            -0.20194884647056455,
            -0.18495460675573647,
            0.39969215206137865
        ],
        [
            -0.20196312971019204,
            -0.18493070093566447,
            0.399672424293096
        ],
        [
            -0.20196102124742948,
            -0.18494779016823704,
            0.39967112755648215
        ]
    ]


class XPAD(Thread):  # def class typr thread
    def __init__(self, semaphore):
        Thread.__init__(self)
        self.semaphore = semaphore
        self.LBumper = 0
        self.RBumper = 0
        self.LStickX = 0
        self.LStickY = 0
        self.RStickX = 0
        self.RStickY = 0
        self.LThumb = 0
        self.A = False
        self.Y = False
        self.Select = False

    def run(self):  # run is a default Thread function
        global end

        while not end:
            for event in get_gamepad():
                with self.semaphore:
                    if event.ev_type == "Key":

                        if event.code == "BTN_THUMBL":
                            self.LThumb = event.state
                        elif event.code == "BTN_TL":
                            self.LBumper = event.state
                        elif event.code == "BTN_TR":
                            self.RBumper = event.state
                        elif event.code == "BTN_WEST":
                            self.Y = bool(event.state)
                            end = True
                        elif event.code == "BTN_SOUTH":
                            self.A = bool(event.state)
                        elif event.code == "BTN_SELECT":
                            self.Select = bool(event.state)

                    elif event.ev_type == "Absolute":  # category of analog values

                        if event.code[-1:] == "Z":
                            event.state = event.state << 1  # reduce range from 256 to 512
                        else:
                            event.state = event.state >> 6  # reduce range from 32000 to 512

                        if 40 > event.state > -40:
                            event.state = 0

                        if event.code == "ABS_X":
                            self.LStickX = event.state
                        elif event.code == "ABS_Y":
                            self.LStickY = event.state
                        elif event.code == "ABS_RX":
                            self.RStickX = event.state
                        elif event.code == "ABS_RY":
                            self.RStickY = event.state


def talker():
    global end
    joint_control = False

    gamePad = XPAD(obj)
    pub = rospy.Publisher('move_command', Float32MultiArray, queue_size=10)
    pub_mov_sphere = rospy.Publisher('move_sphere_command', Float32MultiArray, queue_size=10)
    pub_mov_joint = rospy.Publisher('move_joint', Float32MultiArray, queue_size=10)
    pub_speed_joint = rospy.Publisher('speed_joint', Float32MultiArray, queue_size=10)
    pub_reset = rospy.Publisher('ur5_simulation/reset', Bool, queue_size=10)
    pub_store = rospy.Publisher('store_command', Bool, queue_size=10)
    rospy.init_node(name_node, anonymous=True)
    rate = rospy.Rate(50)  # 50h
    i = 0

    try:
        gamePad.start()

        while not rospy.is_shutdown():
            with obj:
                mult = 1
                if gamePad.LBumper:
                    mult = 0.5
                elif gamePad.RBumper:
                    mult = 2

                aux_y = gamePad.Y
                gamePad.Y = False

                if gamePad.Select:
                    joint_control = not joint_control
                    print("Joint control" if joint_control else "TCP control")

                gamePad.Select = False

                aux_a = gamePad.A
                gamePad.A = False

                x = gamePad.LStickX / mult
                y = -gamePad.LStickY / mult
                z = -gamePad.RStickY / mult
                aux = [x, y, z, 0, 0, 0] if not gamePad.LThumb else [0, 0, 0, x, y, z]

            mess = Float32MultiArray(data=aux)

            # rospy.loginfo(mess)

            if not joint_control:
                pub.publish(mess)
            else:
                pub_speed_joint.publish(mess)

            # if i < len(example):
            #     mess = Float32MultiArray(data=example[i])
            #     pub_mov_sphere.publish(mess)
            #
            #     i += 1
            # else:
            #     i = 0

            if aux_y:
                mess = Bool(data=aux_y)
                pub_store.publish(mess)
                break

            if aux_a:
                mess = Bool(data=aux_a)
                pub_reset.publish(mess)

            rate.sleep()
    finally:
        end = True


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
