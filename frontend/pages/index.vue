<template>
  <div>
   <Tutorial />
    <div v-for="d in dat.person_data" :key=d.person_name align="center">
    <h2>
      {{d.person_name}} {{d.person_age}} 
    </h2>
    </div>
    <div>
      <span @click="CloseAutoScheduleMessage()">自動スケジュール完了</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',

  async asyncData({ $axios }){
    const url = "get_person";
    const response = await $axios.$get(url);   
    return { dat: response};
  },
  
  methods: {
    CloseAutoScheduleMessage(){

    }
  }

}

</script>
