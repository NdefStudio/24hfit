<template>
  <div style="height:100%">
    <x-header slot="header"
              style="width:100%;position:fixed;
              left:0;top:0;z-index:100;background-color:#43c9db;">
      <span>健康管理报告</span>
      <x-icon slot="overwrite-left"
              type="ios-arrow-back"
              size="35"
              style="fill:#fff;position:relative;top:-8px;left:-3px;"
              @click="onClickBack"></x-icon>
    </x-header>
    <div class="panel"
         style="margin-top:50px">
      <group>
        <cell title="每日运动分钟数"></cell>
      </group>
      <v-chart :data="walkdata"
               prevent-default>
        <v-scale x
                 :tick-count="3" />
        <v-tooltip :show-item-marker="false"
                   show-x-value />
        <v-line />
      </v-chart>
      <group>
        <cell title="活动时间比例"></cell>
      </group>
      <v-chart :data="timedata">
        <v-scale y
                 :options="yOptions" />
        <v-tooltip disabled />
        <v-pie :radius="0.85"
               series-field="name" />
        <v-legend :options="legendOptions" />
      </v-chart>
    </div>
  </div>
</template>

<script>
import {
  XHeader,
  VChart,
  VTooltip,
  VLine,
  VScale,
  Cell,
  Group,
  VArea,
  VLegend,
  VBar,
  VPie
} from 'vux'

const map = {
  睡眠: '30%',
  步行: '10%',
  跑步: '6%',
  玩手机: '15%',
  体操: '5%',
  其他: '34%'
}

export default {
  components: {
    XHeader,
    VChart,
    VTooltip,
    VLine,
    VScale,
    Cell,
    Group,
    VArea,
    VLegend,
    VBar,
    VPie
  },

  methods: {
    onClickBack() {
      this.$router.push(`/main/${this.id}/my`)
    }
  },
  data() {
    return {
      id: this.$route.params.id,
      legendOptions: {
        position: 'right',
        itemFormatter(val) {
          return val + '  ' + map[val]
        }
      },
      yOptions: {
        formatter(val) {
          return val * 100 + '%'
        }
      },
      map,
      timedata: [
        { name: '睡眠', percent: 0.3, a: '1' },
        { name: '步行', percent: 0.1, a: '1' },
        { name: '跑步', percent: 0.06, a: '1' },
        { name: '玩手机', percent: 0.15, a: '1' },
        { name: '体操', percent: 0.05, a: '1' },
        { name: '其他', percent: 0.34, a: '1' }
      ],
      walkdata: [
        { date: '2019-06-05', value: 35 },
        { date: '2019-06-06', value: 129 },
        { date: '2019-06-07', value: 135 },
        { date: '2019-06-08', value: 86 },
        { date: '2019-06-09', value: 73 },
        { date: '2019-06-10', value: 85 },
        { date: '2019-06-11', value: 73 },
        { date: '2019-06-12', value: 68 },
        { date: '2019-06-13', value: 92 },
        { date: '2019-06-14', value: 130 },
        { date: '2019-06-15', value: 45 },
        { date: '2019-06-16', value: 139 },
        { date: '2019-06-17', value: 115 },
        { date: '2019-06-18', value: 111 },
        { date: '2019-06-19', value: 142 },
        { date: '2019-06-20', value: 186 },
        { date: '2019-06-21', value: 137 },
        { date: '2019-06-22', value: 128 },
        { date: '2019-06-23', value: 85 },
        { date: '2019-06-24', value: 94 },
        { date: '2019-06-25', value: 71 },
        { date: '2019-06-26', value: 106 },
        { date: '2019-06-27', value: 84 },
        { date: '2019-06-28', value: 93 },
        { date: '2019-06-29', value: 85 },
        { date: '2019-06-30', value: 73 },
        { date: '2019-07-01', value: 83 },
        { date: '2019-07-02', value: 125 },
        { date: '2019-07-03', value: 107 },
        { date: '2019-07-04', value: 82 },
        { date: '2019-07-05', value: 44 },
        { date: '2019-07-06', value: 72 },
        { date: '2019-07-07', value: 106 },
        { date: '2019-07-08', value: 107 },
        { date: '2019-07-09', value: 66 },
        { date: '2019-07-10', value: 91 },
        { date: '2019-07-11', value: 92 },
        { date: '2019-07-12', value: 113 },
        { date: '2019-07-13', value: 107 },
        { date: '2019-07-14', value: 131 },
        { date: '2019-07-15', value: 111 },
        { date: '2019-07-16', value: 64 },
        { date: '2019-07-17', value: 69 },
        { date: '2019-07-18', value: 88 },
        { date: '2019-07-19', value: 77 },
        { date: '2019-07-20', value: 83 },
        { date: '2019-07-21', value: 111 },
        { date: '2019-07-22', value: 57 },
        { date: '2019-07-23', value: 55 },
        { date: '2019-07-24', value: 60 }
      ]
    }
  }
}
</script>

<style>
.panel {
  overflow: scroll;
  -webkit-overflow-scrolling: touch;
}
</style>