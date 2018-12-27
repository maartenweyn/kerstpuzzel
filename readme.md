
## Ceasar code
Tests all possible keys and test if at least tests if at least 60% of the words are in the dictionary


```
python3 ceaser.py "pr ilu kl whwh chu thaapqz lu upuh"

Rotating pr ilu kl whwh chu thaapqz lu upuh

-13 ==> ce vyh xy juju puh gunncdm yh hchu False
-12 ==> df wzi yz kvkv qvi hvooden zi idiv False
-11 ==> eg xaj za lwlw rwj iwppefo aj jejw False
-10 ==> fh ybk ab mxmx sxk jxqqfgp bk kfkx False
 -9 ==> gi zcl bc nyny tyl kyrrghq cl lgly False
 -8 ==> hj adm cd ozoz uzm lzsshir dm mhmz False
 -7 ==> ik ben de papa van mattijs en nina True
 -6 ==> jl cfo ef qbqb wbo nbuujkt fo ojob False
 -5 ==> km dgp fg rcrc xcp ocvvklu gp pkpc False
 -4 ==> ln ehq gh sdsd ydq pdwwlmv hq qlqd False
 -3 ==> mo fir hi tete zer qexxmnw ir rmre False
 -2 ==> np gjs ij ufuf afs rfyynox js snsf False
 -1 ==> oq hkt jk vgvg bgt sgzzopy kt totg False
 +0 ==> pr ilu kl whwh chu thaapqz lu upuh False
 +1 ==> qs jmv lm xixi div uibbqra mv vqvi False
 +2 ==> rt knw mn yjyj ejw vjccrsb nw wrwj False
 +3 ==> su lox no zkzk fkx wkddstc ox xsxk False
 +4 ==> tv mpy op alal gly xleetud py ytyl False
 +5 ==> uw nqz pq bmbm hmz ymffuve qz zuzm False
 +6 ==> vx ora qr cncn ina znggvwf ra avan False
 +7 ==> wy psb rs dodo job aohhwxg sb bwbo False
 +8 ==> xz qtc st epep kpc bpiixyh tc cxcp False
 +9 ==> ya rud tu fqfq lqd cqjjyzi ud dydq False
+10 ==> zb sve uv grgr mre drkkzaj ve ezer False
+11 ==> ac twf vw hshs nsf esllabk wf fafs False
+12 ==> bd uxg wx itit otg ftmmbcl xg gbgt False
+13 ==> ce vyh xy juju puh gunncdm yh hchu False
Found it  -7 ==> ik ben de papa van mattijs en nina
```



##Transposition code

Tests all posible transpositions from 2 to length of cyper and tests if at least 60% of the words are in the dictionary

```
python3 transposition.py "ieajnk nsa p   bame epan nat    tn dvii "

  2 ==> ieepaajnn kn ants a   p  t n  bdavmiei   False
  3 ==> i teb aa jm ne k t ennp sadanv  ipni a   False
  4 ==> i e epp a atj nnn   kbnd aavnmtise ia    False
  5 ==> isa teamnna ea jp tdn e vk p i  a inbn   False
  6 ==> in p  esba daaan vj m  inpentik  an   et False
  7 ==> i  e  den  n vas eatijabptnin aa   kpmn  False
  8 ==> ik ben de papa van mattijs en nina       True
  9 ==> ik be  tve papn nian maa  ijs ent d na   False
 10 ==> ins ae  tveka mpn nia   eaa  ijnpb nt d  False
 11 ==> ins ae    ieka mpn tdia   eaa nv jnpb nt False
 12 ==> ins a an   ieka mena tdia   ep t nv jnpb False
 13 ==> inn  a an   ieksp mena tdia a bep t nv j False
 14 ==> ij a bep t nvienn  a an   i aksp mena td False
 15 ==> ij a bep t t vienn  a an  ndi aksp mena  False
 16 ==> ij a bep a  t vienn  a ant  ndi aksp men False
 17 ==> ij a beea a  t vienn  a pnnt  ndi aksp m False
 18 ==> ij a  aeea a  t vienn  bm pnnt  ndi aksp False
 19 ==> ij s   aeea a  t viennap bm pnnt  ndi ak False
 20 ==> ian s   aeea a  t viejknap bm pnnt  ndi  False
 21 ==> ian s   aeea a  t vi ejknap bm pnnt  ndi False
 22 ==> ian s   aeea a  t vii ejknap bm pnnt  nd False
 23 ==> ian s   aeea a  t dvii ejknap bm pnnt  n False
 24 ==> ian s   aeea a  tn dvii ejknap bm pnnt   False
 25 ==> ian s   aeea a   tn dvii ejknap bm pnnt  False
 26 ==> ian s   aeea a    tn dvii ejknap bm pnnt False
 27 ==> ian s   aeea at    tn dvii ejknap bm pnn False
 28 ==> ian s   aeea nat    tn dvii ejknap bm pn False
 29 ==> ian s   aeean nat    tn dvii ejknap bm p False
 30 ==> ian s   aeepan nat    tn dvii ejknap bm  False
 31 ==> ian s   ae epan nat    tn dvii ejknap bm False
 32 ==> ian s   ame epan nat    tn dvii ejknap b False
 33 ==> ian s   bame epan nat    tn dvii ejknap  False
 34 ==> ian s    bame epan nat    tn dvii ejknap False
 35 ==> ian s p   bame epan nat    tn dvii ejkna False
 36 ==> ian sa p   bame epan nat    tn dvii ejkn False
 37 ==> ian nsa p   bame epan nat    tn dvii ejk False
 38 ==> iank nsa p   bame epan nat    tn dvii ej False
 39 ==> iajnk nsa p   bame epan nat    tn dvii e False

```