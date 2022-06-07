<template>
  <application-menu>
    <vue-perfect-scrollbar
      :settings="{ suppressScrollX: true, wheelPropagation: false }"
    >
      <div class="p-4">
        <div v-for="(filterItem, index) in filters">
          <label>{{ filterItem.title }}</label>
          <b-form-checkbox-group
            v-model="selectedFilters"
            stacked
            class="list-unstyled mb-4"
          >
            <b-form-checkbox
              v-for="(tag, index) in filterItem.tags"
              :name="filterItem.title"
              :value="tag.id"
              >{{ tag.title }}</b-form-checkbox
            >
          </b-form-checkbox-group>
        </div>

        <div v-for="(filterItem, index) in subCategories">
          <label>{{ filterItem.title }}</label>
          <b-form-checkbox-group
            v-model="selectedsubCategories"
            stacked
            class="list-unstyled mb-4"
          >
            <b-form-checkbox
              v-for="(tag, index) in filterItem.tags"
              :name="filterItem.title"
              :value="tag.id"
              >{{ tag.title }}</b-form-checkbox
            >
          </b-form-checkbox-group>
        </div>
      </div>
    </vue-perfect-scrollbar>
  </application-menu>
</template>
<script>
import ApplicationMenu from "../components/Common/ApplicationMenu";
import axios from "axios";
import { apiUrl, api } from "../constants/config";

const TodoApplicationMenu = {
  props: ["categories", "labels", "items", "categoryID", "loadFiltersR"],
  components: {
    "application-menu": ApplicationMenu
  },
  data() {
    return {
      tags: [],
      filters: [],
      subCategories: [],
      filter: [],
      selectedFilters: [],
      selectedsubCategories: [],
      options1: [
        { text: "paid", value: "first" },
        { text: "free", value: "second" }
      ],
      options2: [
        { text: "video", value: "first" },
        { text: "book", value: "second" }
      ],
      options3: [
        { text: "beginner", value: "first" },
        { text: "advanced", value: "second" }
      ]
    };
  },
  watch: {
    selectedFilters() {
      this.loadFiltersR(this.selectedFilters, this.selectedsubCategories);
    },
    selectedsubCategories() {
      this.loadFiltersR(this.selectedFilters, this.selectedsubCategories);
    }
  },
  methods: {
    loadFilters() {
      console.log();

      axios
        .get(api + "ListTags/")
        .then(response => {
          console.log("tags list");
          console.log(response);
          return response.data;
        })
        .then(res => {
          this.tags = res;
          for (var i = 0; i < res.length; i++) {
            if (!this.filter.includes(res[i].type)) {
              this.filter.push(res[i].type);
            }
          }
          for (var j = 0; j < this.filter.length; j++) {
            var temp = [];
            for (var i = 0; i < this.tags.length; i++) {
              if (this.filter[j] == this.tags[i].type) {
                temp.push(this.tags[i]);
              }
            }
            this.filters.push({ title: this.filter[j], tags: temp });
          }
          console.log("filters");
          console.log(this.filters);
        });
    },

    loadSubCategory() {
      const data = {
        categoryId: this.categoryID
      };

      axios
        .post(api + "subcategoryList/", data)
        .then(response => {
          return response.data;
        })
        .then(res => {
          this.subCategories.push({ title: "subcategory", tags: res });
          console.log(this.filters);
        });
    }
  },
  mounted() {
    document.body.classList.add("right-menu");
    this.loadFilters();
    this.loadSubCategory();
  },
  beforeDestroy() {
    document.body.classList.remove("right-menu");
  }
};
export default TodoApplicationMenu;
</script>
