<template>
  <b-card overlay style="height: 200px;background-color:#006da3;" class="img-fluid mb-2" alt="Responsive image"
    text-variant="white">
    <b-card-body>
      <center>
        <h2 class="card-title text-white">Find the best software engineering courses & tutorials</h2>
      </center>
      <b-form class="form-container">
        <b-form-group>
          <b-form-input type="text" :placeholder="'search for software engineering categories...'"
            @input="(val) => searchChange(val)"></b-form-input>
        </b-form-group>
      </b-form>
    </b-card-body>
  </b-card>
</template>
<script>
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";

export default {
  components: {
    "v-select": vSelect
  },
  props: [
    "searchChange",

  ],
  data() {
    return {
      selectData: [
        {
          label: "Chocolate",
          value: "chocolate"
        },
        {
          label: "Vanilla",
          value: "vanilla"
        },
        {
          label: "Strawberry",
          value: "strawberry"
        },
        {
          label: "Caramel",
          value: "caramel"
        },
        {
          label: "Cookies and Cream",
          value: "cookiescream"
        },
        {
          label: "Peppermint",
          value: "peppermint"
        }
      ]
    };
  },
  methods: {

  }
};
</script>
