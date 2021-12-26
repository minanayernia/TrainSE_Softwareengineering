
<template>
  <div class="disable-text-selection">
    <todo-application-menu v-if="isLoad" :loadFiltersR="loadFiltersR" :items="items" :categories="categories" :labels="labels" :categoryID="categoryID" ></todo-application-menu>

  <b-row class="app-row survey-app">
    <b-colxx class="disable-text-selection">
      <list-page-heading
        :title="$t('Category Name')"
        :selectAll="selectAll"
        :isSelectedAll="isSelectedAll"
        :isAnyItemSelected="isAnyItemSelected"
        :keymap="keymap"
        :displayMode="displayMode"
        :changeDisplayMode="changeDisplayMode"
        :changeOrderBy="changeOrderBy"
        :changePageSize="changePageSize"
        :sort="sort"
        :searchChange="searchChange"
        :from="from"
        :to="to"
        :total="total"
        :perPage="perPage"
        :categoryID="categoryID"
        :loadItems="loadItems"
        :currentUser="currentUser"
      ></list-page-heading>
      <template v-if="isLoad">
        <list-page-listing
          :displayMode="displayMode"
          :items="items"
          :selectedItems="selectedItems"
          :toggleItem="toggleItem"
          :lastPage="lastPage"
          :perPage="perPage"
          :page="page"
          :changePage="changePage"
          :handleContextMenu="handleContextMenu"
          :loadItems="loadItems"
          :onContextMenuAction="onContextMenuAction"
          :currentUser="currentUser"
        ></list-page-listing>
      </template>
      <template v-else>
        <div class="loading"></div>
      </template>
    </b-colxx>

  </b-row>
  </div>

</template>

<script>
import axios from "axios";
import { apiUrl ,api } from "../../../../constants/config";
import ListPageHeading from "../../../../containers/pages/ListPageHeading";
import ListPageListing from "../../../../containers/pages/ListPageListing";
import TodoApplicationMenu from "../../../../containers/applications/TodoApplicationMenu_filter";
import { mapGetters, mapMutations, mapActions } from "vuex";


export default {
  components: {
    "list-page-heading": ListPageHeading,
    "list-page-listing": ListPageListing,
    "todo-application-menu":TodoApplicationMenu
  },
  data() {
    return {
      resourceList:[],
      isLoad: false,
      apiBase: apiUrl + "/cakes/fordatatable",
      displayMode: "image",
      sort: {
        column: "title",
        label: "Rating"
      },
      page: 1,
      categoryID:this.$route.params.id,
      perPage: 4,
      search: "",
      from: 0,
      to: 0,
      total: 0,
      lastPage: 0,
      items: [],
      selectedItems: [],
      categories: [
        {
          label: "Free",
          value: "Free"
        },
        {
          label: "Beginner",
          value: "Beginner"
        },
        {
          label: "Book",
          value: "Book"
        },
        {
          label: "Python3",
          value: "Python3"
        }
      ],
      labels: [
        {
          label: "JAVA",
          value: "JAVA",
          color: "secondary"
        },
        {
          label: "PAID",
          value: "PAID",
          color: "primary"
        },
        {
          label: "ADVANCED",
          value: "ADVANCED",
          color: "info"
        }
      ],
    };
  },

  methods: {
    loadFiltersR(tags,subcategories){
      const data={
        categoryId:this.$route.params.id,
        tags:tags,
        subcategories:subcategories

      };
      axios
        .post(api+"filterResourceList/",data)
        .then(response => {
          console.log("resource list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.items= res;
            this.isLoad=true;
            console.log(res);
        });
    },
    loadItems() {
      console.log(this.currentUser)
      const data={
          categoryId:this.$route.params.id,
          personId:null,
      };

      if(this.currentUser != null){

        data.personId=this.currentUser.id;
      }
      
      axios
        .post(api+"resourceList/",data)
        .then(response => {
          console.log("resource list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.items= res;
            this.isLoad=true;
            console.log(res);
        });
    },

    searchResource(val){
      
    },

    changeDisplayMode(displayType) {
      this.displayMode = displayType;
    },
    changePageSize(perPage) {
      this.page = 1;
      this.perPage = perPage;
    },
    changeOrderBy(sort) {
      this.sort = sort;
    },
    searchChange(val) {
      
      console.log("searchResource");
      console.log(val);
      const data={
        text:val,
        categoryID:this.$route.params.id,
      };
      axios
        .post(api+"searchResource/",data)
        .then(response => {
          console.log("search resource");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.items = res;
            console.log(this.items);
            console.log(res);
        });
    },

    selectAll(isToggle) {
      if (this.selectedItems.length >= this.items.length) {
        if (isToggle) this.selectedItems = [];
      } else {
        this.selectedItems = this.items.map(x => x.id);
      }
    },
    keymap(event) {
      switch (event.srcKey) {
        case "select":
          this.selectAll(false);
          break;
        case "undo":
          this.selectedItems = [];
          break;
      }
    },
    getIndex(value, arr, prop) {
      for (var i = 0; i < arr.length; i++) {
        if (arr[i][prop] === value) {
          return i;
        }
      }
      return -1;
    },
    toggleItem(event, itemId) {
      if (event.shiftKey && this.selectedItems.length > 0) {
        let itemsForToggle = this.items;
        var start = this.getIndex(itemId, itemsForToggle, "id");
        var end = this.getIndex(
          this.selectedItems[this.selectedItems.length - 1],
          itemsForToggle,
          "id"
        );
        itemsForToggle = itemsForToggle.slice(
          Math.min(start, end),
          Math.max(start, end) + 1
        );
        this.selectedItems.push(
          ...itemsForToggle.map(item => {
            return item.id;
          })
        );
      } else {
        if (this.selectedItems.includes(itemId)) {
          this.selectedItems = this.selectedItems.filter(x => x !== itemId);
        } else this.selectedItems.push(itemId);
      }
    },
    handleContextMenu(vnode) {
      if (!this.selectedItems.includes(vnode.key)) {
        this.selectedItems = [vnode.key];
      }
    },
    onContextMenuAction(action) {
      console.log(
        "context menu item clicked - " + action + ": ",
        this.selectedItems
      );
    },
    changePage(pageNum) {
      this.page = pageNum;
    }
  },

  computed: {
        ...mapGetters({
      currentUser: "currentUser",
      menuType: "getMenuType",
      menuClickCount: "getMenuClickCount",
      selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    }),
    isSelectedAll() {
      return this.selectedItems.length >= this.items.length;
    },
    isAnyItemSelected() {
      return (
        this.selectedItems.length > 0 &&
        this.selectedItems.length < this.items.length
      );
    },
    apiUrl() {
      return `${this.apiBase}?sort=${this.sort.column}&page=${this.page}&per_page=${this.perPage}&search=${this.search}`;
    }
  },
  watch: {
    search() {
      this.page = 1;
    },
    apiUrl() {
      this.loadItems();
    }
  },
  mounted() {
    this.loadItems();
    
  }
};
</script>
