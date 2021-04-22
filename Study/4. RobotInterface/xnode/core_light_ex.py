from pop import Light
import time

l = Light()

light_table = {
    'A':'어두운 분위기 중의 시식별 작업장',
    'B':'어두운 분기기의 이용이 빈번하지 않은 장소',
    'C':'어두운 분위기의 공공 장소',
    'D':'잠시 동안의 단순 작업장',
    'E':'시작업이 빈번하지 않은 작업장',
    'F':'고휘도 대비 혹은 큰 물체 대상의 시작업 수행',
    'G':'일반휘도 대비 혹은 큰 물체 대상의 시작업 수행',
    'H':'저휘도 대비 혹은 매우 작은 물체 대상의 시작업 수행',
    'I':'비교적 장시간 동안 저휘도 대비 혹은 매우 작은 물체 대상의 시작업 수행',
    'J':'장시간 동안 힘든 시작업 수행',
    'K':'희도 대비가 거의 안되며 작은 물체의 매우 특별한 시작업 수행'
}

for _ in range(10):
    val = l.read()
    ret = None
    
    if val >= 3 and val <= 6:
        ret = light_table['A']
    elif val > 6 and val <= 15:
        ret = light_table['B']
    elif val > 15 and val <= 30:
        ret = light_table['C']
    elif val > 30 and val <= 60:
        ret = light_table['D']
    elif val > 60 and val <= 150:
         ret = light_table['E']
    elif val > 150 and val <= 300:
         ret = light_table['F']
    elif val > 300 and val <= 600:
        ret = light_table['G']
    elif val > 600 and val <= 1500:
        ret = light_table['H']
    elif val > 1500 and val <= 3000:
        ret = light_table['I']
    elif val > 3000 and val <= 6000:
        ret = light_table['J']
    elif val > 6000 and val <= 15000:
        ret = light_table['K']
    
    print("light = %d lx, level = %s"%(val, ret))
    time.sleep(1)