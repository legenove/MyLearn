/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PromotePlansId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
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
            url: "/promote_plans/" + obj.id + "",
            method: "GET",
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
            id   'integer' int id in query
            item_id   'ref' 
            valid   'ref' 
            
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
            url: "/promote_plans/" + obj.id + "",
            method: "POST",
            data: {
                item_id: obj.item_id,
                valid: obj.valid
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
            id   'integer' int id in query
            status   'string' 
            
        @success
            status 200    type:object
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/promote_plans/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status
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
    PromotePlansId: new PromotePlansId
};