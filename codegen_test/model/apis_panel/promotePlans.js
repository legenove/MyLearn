/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PromotePlans = function () {
    /*
        @params obj 'data params'
            status   'string' plan status in query
            date_executed   'string' date executed in query
            operator_id   'integer' operator id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            total_items   'ref' 
            status   'ref' 
            operator_id   'ref' 
            plan_type   'string' 
            cost   'ref' 
            promote_items   'ref' 
            date_created   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/promote_plans",
            method: "GET",
            data: {
                status: obj.status,
                date_executed: obj.date_executed,
                operator_id: obj.operator_id,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    
    /*
        @params obj 'data params'
            max_cost   'integer' 
            round_off   'string' 
            plan_type   'string' 
            budget   'integer' 
            duration   'integer' 
            clean_plan_id   'integer' 
            date_executed   'string' 
            
        @success
            status 201    type:object
            total_items   'ref' 
            status   'ref' 
            operator_id   'ref' 
            plan_type   'string' 
            cost   'ref' 
            promote_items   'ref' 
            date_created   'ref' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/promote_plans",
            method: "POST",
            data: {
                max_cost: obj.max_cost,
                round_off: obj.round_off,
                plan_type: obj.plan_type,
                budget: obj.budget,
                duration: obj.duration,
                clean_plan_id: obj.clean_plan_id,
                date_executed: obj.date_executed
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    PromotePlans: new PromotePlans
};