<template>
  <div>
    <group>
      <div class="userpanel">
        <img class="avator"
             src="../assets/avator.png"
             alt="用户头像" />
        <div style="flex-direction:colomn">
          <p class="maintext">{{username}}</p>
          <p class="subtext">{{quote}}</p>
        </div>
      </div>
      <cell title="性别：">{{gender=='m'?'男':'女'}}</cell>
      <cell title="身高：">{{height+'厘米'}}</cell>
      <cell title="体重：">{{weight+'千克'}}</cell>
      <cell title="年龄：">{{age+'岁'}}</cell>
    </group>
    <group>
      <cell title="健康状态：">{{healthstatus}}</cell>
      <cell title="我的时间报告"
            :link="{path:`/report/${id}`}"></cell>
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
      id: this.$route.params.id,
      usetime: '',
      gender: '',
      height: '',
      weight: '',
      age: '',
      healthstatus: ''
    }
  },
  mounted() {
    // 这里开始发送用户信息请求
    this.$axios
      .get(this.global.apiserver + 'usr', {
        params: {
          id: this.global.id
        }
      })
      .then(response => {
        console.log(response)
        this.username = response.data.username
        this.quote = response.data.quote
        this.usetime = response.data.usetime
        this.gender = response.data.gender
        this.height = response.data.height
        this.weight = response.data.weight
        this.age = response.data.age
        this.healthstatus = response.data.healthstatus
      })
      .catch(error => {
        console.log(error)
      })

    console.log(this.usetime)
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