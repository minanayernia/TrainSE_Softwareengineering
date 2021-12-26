<template>
  <div>
    <b-row>
      <b-colxx lg="1" md="1" xl="1" sm="1">
      </b-colxx>
      <b-colxx lg="10" md="10" xl="10" sm="10" class="mb-4">
        <advanced-search :searchChange="searchChange"></advanced-search>
      </b-colxx>

    </b-row>
    <b-row>
      <b-colxx lg="1" md="1" xl="1" sm="1">
      </b-colxx>
      <b-colxx  lg="10" md="10" xl="10" sm="10" class="mb-4">
      
        <b-row>
          <b-colxx v-for="(category,index) in categoryList" :key="index" md="4" sm="6" lg="3" xxs="12">
            <b-card  class="mb-4 text-center">
              <router-link :to="`/app/pages/product/image-list/${category.category_id}`" >
                <img
                  :src="category.image"
                  alt="Card image cap"
                  class="img-thumbnail list-thumbnail rounded-circle border-0 mb-4"
                />
                <h6 class="mb-1 card-subtitle">{{category.title}}</h6>
              </router-link>
            </b-card>
          </b-colxx>
        </b-row>
      </b-colxx>
    </b-row>
  </div>
</template>

<script>
import AdvancedSearch from "../../../containers/dashboards/AdvancedSearch";
import axios from "axios";
import { api } from "../../../constants/config";
import data from '../../../constants/menu';
export default {
  components: {
    "advanced-search": AdvancedSearch,

  },
  data(){

    return{
      apiBase: api + "categoryList/",

      categoryList:[]
    }
  },
  methods: {
    getCategories() {
                console.log("category list");

      axios
        .get(this.apiBase)
        .then(response => {
          console.log("category list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.categoryList = res;
            console.log(res);
        });
    },
    searchChange(val) {
      console.log("search");
      console.log(val);
      const data={
        text:val
      };
      axios
        .post(api+"searchCategory/",data)
        .then(response => {
          console.log("search list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.categoryList = res;
            console.log(res);
        });
    },
  },
  mounted() {
    this.getCategories();
  }
};
</script>
