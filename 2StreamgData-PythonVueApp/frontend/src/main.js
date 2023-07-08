import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App)


app.mount("#app")

{/* <template>
  <div>
    <h1>{{ info }}</h1>
    <button @click="clicked">Press</button>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data () {
    return {
      info: ""
    }
  },
  methods:{
    async clicked(){
      try {
        const eventSource = new EventSource('http://localhost:8000/stream');
        eventSource.onmessage = (event) => {
          const digit = event.data.trim();
          this.info += digit;
        };
      } catch (error) {
        console.error(error);
      }
    }
  },
  mounted () {
    this.info = "Click for Action "
  }
}
</script> */}
