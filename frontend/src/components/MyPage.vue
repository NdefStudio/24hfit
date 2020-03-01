<template>
  <div>
    <group>
      <div class="userpanel">
        <img class='avator'
             src="../assets/avator.png"
             alt="用户头像">
        <div style="flex-direction:colomn">
          <p class="maintext">{{username}}</p>
          <p class="subtext">{{quote}}</p>
        </div>
      </div>
      <cell title="使用时间：">{{usetime}}</cell>

    </group>
    <group>
      <cell title="我的时间报告"
            :link="{path:'/main/report/'+userid}">
      </cell>
    </group>
  </div>
</template>

<script>
import { Cell, Group } from 'vux'

export default {
  components: { Cell, Group },
  data() {
    return {
      username: '约翰史密斯',
      quote: '做时间的主人，过健康的生活',
      userid: '1241531',
      usetime: '24h'
    }
  }
}
</script>

<style>
.avator {
  height: 120px;
  width: 120px;
  margin-right: 20px;
}
.userpanel {
  display: flex;
  flex-direction: row;
  padding: 20px;
}
.maintext {
  margin-top: 15px;
  font-size: 25px;
}
.subtext {
  margin-top: 20px;
  font-size: 18px;
  color: grey;
}
</style>