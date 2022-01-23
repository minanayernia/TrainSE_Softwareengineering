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

          <b-colxx v-if="currentUser.role=='A'" md="4" sm="6" lg="3" xxs="12">
            <b-card  class="mb-4 text-center" v-b-modal.modalright>
                <img
                  src="https://cdn4.iconfinder.com/data/icons/user-interface-131/32/add-512.png"
                  alt="Card image cap"
                  class="img-thumbnail list-thumbnail rounded-circle border-0 mb-4"
                />
                <h6 class="mb-1 card-subtitle">Add New</h6>

            </b-card>
          </b-colxx>

          <b-colxx v-for="(category,index) in categoryList" :key="index" md="4" sm="6" lg="3" xxs="12" >
            <b-card  class="mb-4 text-center"  >
              <router-link :to="{ name: 'resource-list', params: { id: category.category_id , name:category.title }}"  >
              
                <img
                  src="https://www.iceye.com/hubfs/Blog/Software_Engineering.jpg"
                  alt="Card image cap"
                  class="img-thumbnail list-thumbnail rounded-circle border-0 mb-4"
                />
                <h6 class="mb-1 card-subtitle">{{category.title}}</h6>
              </router-link>
                <hr v-if="currentUser.role=='A'"/>
                <b-row v-if="currentUser.role=='A'">
                  <b-colxx  lg="6">
                    <b-button  variant="outline-primary" class="btn  btn-block  default text-center rounded" @click="changeId(category.category_id)" v-b-modal.modall
                      ><i class="fa fa-edit fa-fw fa-lg"></i></b-button>
                  </b-colxx>
                  <b-colxx  lg="6">
                  <b-button  variant="outline-primary" class="btn  btn-block  default text-center rounded" @click="deletee(category.category_id)"
                    ><i class="fa fa-trash fa-lg"></i></b-button
                  >
                </b-colxx>            
              </b-row>
            </b-card>

          </b-colxx>
          <add-new-modal @update="getCategories" ></add-new-modal>
          <Edit @update="getCategories" :ItemID="cat_ID"></Edit>

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
import AddNewModal from "./AddNewModal";
import Edit from "./Edit";
import { mapGetters, mapMutations, mapActions } from "vuex";

export default {
  components: {
    "advanced-search": AdvancedSearch,
    "add-new-modal": AddNewModal,
    "Edit": Edit,
  },
  data(){
    return{
      apiBase: api + "categoryList/",
      cat_ID:0,
      isHovered:false,
      categoryList:[],
      id:0,
    }
  },
  methods: {
    changeId(id){
      console.log("id")
      console.log(this.cat_ID)
      this.cat_ID=id;
      console.log(this.cat_ID)
    },
    deletee(id){
      const data={
        id:id,
      }
      axios
        .post(api + "deleteCategory/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.getCategories();
        });
    },
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
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser",
      menuType: "getMenuType",
      menuClickCount: "getMenuClickCount",
      selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    }),

  },
};
</script>
