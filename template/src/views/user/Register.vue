
<template>
<b-row class="h-100">
    <b-colxx xxs="12" md="10" lg="7" xxl="6" class="mx-auto my-auto" style="margin:5em auto !important;">
        <b-card class="auth-card " no-body>
                <div class="form-side rounded" style="width:100%;">

                <router-link tag="a" to="/">
                    <span class="logo-single" />
                </router-link>
            <h6 class="mb-4">{{ $t('user.register')}}</h6>
                <b-form @submit.prevent="formSubmit" class="av-tooltip tooltip-label-bottom">

                    <b-form-group :label="$t('user.email')" class="has-float-label mb-4">
                        <b-form-input type="text" v-model="$v.form.email.$model" :state="!$v.form.email.$error" />
                        <b-form-invalid-feedback v-if="!$v.form.email.required">Please enter your email address</b-form-invalid-feedback>
                        <b-form-invalid-feedback v-else-if="!$v.form.email.email">Please enter a valid email address</b-form-invalid-feedback>
                    </b-form-group>

                    <b-form-group label="user-name" class="has-float-label mb-4">
                        <b-form-input   type="text" v-model="$v.form.username.$model" :state="!$v.form.username.$error" />
                        <b-form-invalid-feedback v-if="!$v.form.username.required">please enter your username.</b-form-invalid-feedback>
                        <b-form-invalid-feedback v-else-if="!$v.form.username.maxLength">it's too long</b-form-invalid-feedback>
                    </b-form-group>
                    
                    <b-form-group label="password" class="has-float-label mb-4">
                        <b-form-input   type="password" v-model="$v.form.password.$model" :state="!$v.form.password.$error" />
                        <b-form-invalid-feedback v-if="!$v.form.password.required">please enter password.</b-form-invalid-feedback>
                        <b-form-invalid-feedback v-else-if="!$v.form.password.maxLength || !$v.form.password.maxLength">it's too long</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label="repeat password" class="has-float-label mb-4">
                        <b-form-input   type="password" v-model="$v.form.repeatPassword.$model" :state="!$v.form.repeatPassword.$error" />
                        <b-form-invalid-feedback v-if="!$v.form.repeatPassword.sameAs">it's wrong.</b-form-invalid-feedback>
                    </b-form-group>
                    <div class="d-flex justify-content-between align-items-center">
                        <router-link tag="a" to="/user/login">Login</router-link>
                        <b-button type="submit" variant="primary" size="lg" >
                            <span class="label">register</span>
                        </b-button>
                    </div>
                </b-form>
        </div>
      </b-card>
    </b-colxx>
  </b-row>
</template>

<script>
import {
    mapGetters,
    mapActions
} from "vuex";
import {
    validationMixin
} from "vuelidate";
import { api } from '../../constants/config';
const {
    required,
    maxLength,
    minLength,
    email,
    sameAs
} = require("vuelidate/lib/validators");

export default {
    data() {
        return {
            form: {
                email:"",
                username: "",
                phonenumber: "",
                password: "",
                repeatPassword: "",
            },
        };
    },
    mixins: [validationMixin],
    validations: {
        form: {

            email:{
                required,
                email,
            },
            username: {
                required,
                maxLength: maxLength(30)
            },
            password: {
              required,
              maxLength: maxLength(10),
            },
            repeatPassword: {
              sameAsPassword: sameAs('password')
            },

        }
    },
    computed: {
        ...mapGetters(["processing", "loginError"])
    },
    methods: {
        ...mapActions(["login", "register"]),
        formSubmit() {
        this.$v.$touch();
        this.$v.form.$touch();
        if (!this.$v.form.$anyError) {
            this.register({
            username: this.form.username,
            password: this.form.password,
            email: this.form.email,
            role: "U",
            });
        }
        },
    },
    watch: {

        loginError(val) {
            if (val != null) {
                this.$notify("error", "error in register", val, {
                    duration: 3000,
                    permanent: false
                });

            }
        }
    }
};
</script>
