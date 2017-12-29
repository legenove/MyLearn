/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AlbumsAlbumIdItems = function () {
    /*
        @params obj 'data params'
            album_id   'string' album id in path
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            item_id   'string' 
            item_type   'string' 
            album_id   'string' 
            order_score   'integer' 
            item   'string' json化的字典，由item_type决定
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums/" + obj.album_id + "/items",
            method: "GET",
            data: {
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
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
            album_id   'string' album id in path
            items_data   'array' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums/" + obj.album_id + "/items",
            method: "POST",
            data: {
                items_data: obj.items_data
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
    AlbumsAlbumIdItems: new AlbumsAlbumIdItems
};