<template>
  <div>
    <h1>{{ info }}</h1>
    <button @click="clicked">Press</button>
    <div id="app">
      {{ this.dataSource }}
  <table>
    <tr>
      <th>Type</th>
      <th>Timestamp</th>
      <th>Value</th>
    </tr>
    <tr v-for="item in dataset" :key="item.timestamp">
      <td>{{item.type}}</td>
      <td>{{item.timestamp}}</td>
      <td>{{item.value}}</td>
    </tr>
  </table>
</div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data () {
    return {
      info: "",
      dataset:[],
      dataSource:[]
    }
  },
  methods:{

    async mockDataSource(typesSet) {
 const dataset = []

  const timer = setInterval(() => {
    const randomType = typesSet[Math.round(Math.random() * (typesSet.length - 1))]

    dataset.push({
      type: randomType,
      timestamp: Date.now(),
      value: Math.random().toString(32).substr(2)
    })
  }, 1e3)

  return {
    dataset,
    stop() {
      clearInterval(timer)
    }
  }
},
    async clicked() {
      try {
       const response = await fetch("http://localhost:8000/stream");
       // const response = await fetch("http://localhost:5000/stream");
       this.mockDataSource(Array(10).fill(1).map((_, i) => `type${i + 1}`))
        const reader = response.body.getReader();
        let result = "";
        while (true) {
          const { done, value } = await reader.read();
          if (done) {
            break;
          }
          result = new TextDecoder().decode(value);
          this.info = result;
        }
      } catch (error) {
        console.error(error);
      }
    
    },
  },
  mounted () {
    this.info = "Click for Action "
    this.dataSource = this.mockDataSource(Array(10).fill(1).map((_, i) => `type${i + 1}`))
  }
}
</script>
