<template>
  <div>
    <group>
      <x-input title="用户名"
               v-model="username"></x-input>
      <x-input title="密码"
               v-model="password"></x-input>
      <flexbox>
        <flexbox-item></flexbox-item>
        <flexbox-item>
          <x-button type="primary"
                    :show-loading="loading"
                    @click.native="onLogin">登录</x-button>
        </flexbox-item>
        <flexbox-item></flexbox-item>
      </flexbox>
      <cell :value="authword"></cell>
    </group>
  </div>
</template>

<script>
import { XInput, Group, XButton, Flexbox, FlexboxItem, Cell } from 'vux'
export default {
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      auth: false,
      authword: ''
    }
  },
  components: {
    XInput,
    Group,
    XButton,
    Flexbox,
    FlexboxItem,
    Cell
  },
  methods: {
    onLogin: function() {
      // console.log(this.username)
      // console.log(this.password)
      this.loading = true
      // console.log(this.loading)
      // 就在这里发送登录请求
      this.loading = false
      // console.log(this.loading)
      var id = 13324
      this.auth = true
      if (this.auth) {
        this.$router.push({ path: '/main/' + id + '/routine' })
      } else {
        this.authword = '验证失败，请检查用户名密码'
      }
    }
  }
}
</script>

<style>
</style>